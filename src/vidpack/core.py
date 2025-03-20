import json
import re
import shutil
from pathlib import Path

from ffmpeg import FFmpeg, FFmpegError, Progress  # type: ignore
from rich.console import Console
from rich.progress import Progress as ProgressBar

from .constants import Constants
from .helpers import add_affixes, ffmpeg_required
from .models import CompressParams
from .utils import convert_quality_to_crf

console = Console()


def _rethrow_ffmpeg_error(error: FFmpegError) -> None:
    """
    Rethrow an FFmpegError if the error message matches the pattern.
    Args:
        error (FFmpegError): The FFmpegError to be rethrow.
    """

    # For more context, refer to: https://github.com/ivansaul/compress-video/pull/3
    pattern = Constants.FFMPEG_FILE_ALREADY_EXISTS_ERROR_PATTERN
    match = re.search(pattern, error.message, re.IGNORECASE)

    if not match:
        raise error


def _get_duration(path: str | Path) -> float:
    """
    Get the duration of a video file using FFmpeg.
    Args:
        path (str | Path): The path to the video file.

    Returns:
        float: The duration of the video in seconds.
    """
    ffprobe = FFmpeg(executable="ffprobe").input(
        path,
        print_format="json",
        show_streams=None,
    )
    media = json.loads(ffprobe.execute())
    duration = media["streams"][0]["duration"]
    return float(duration)


def _get_progress_percentage(progress: Progress, duration: float) -> float:
    """
    Calculate the progress percentage of a video file using FFmpeg.

    Args:
        progress (Progress): The progress object returned by FFmpeg.
        duration (float): The duration of the source video file in seconds.

    Returns:
        float: The progress percentage as a float between 0 and 100.
    """
    current_time = progress.time.total_seconds()
    return round(current_time / duration * 100)


@ffmpeg_required
def compress_video(params: CompressParams) -> None:
    """
    Compress a video file using FFmpeg and display the progress in a terminal.

    :params: CompressParams
    """

    dst = params.dst if params.dst else params.default_dst

    if not dst.suffix:
        raise Exception("Invalid argument: Output must be a file")

    if dst.exists() and not params.overwrite:
        console.print(
            "⠹ Processing...",
            f"[{params.src.name}]",
            "[File already exists]",
            style="green",
            markup=False,
        )
        return

    tmp = add_affixes(dst, suffix=".tmp")

    crf = convert_quality_to_crf(params.quality)

    ffmpeg = (
        FFmpeg()
        .option("y" if params.overwrite else "n")
        .input(params.src)
        .output(
            tmp,
            vcodec=params.vcodec.value,
            acodec="aac",
            crf=crf,
        )
    )

    console.print(
        "⠹ Processing...",
        f"[{params.src.name}]",
        style="green",
        markup=False,
    )

    with ProgressBar() as progress_bar:
        task = progress_bar.add_task("", total=100, completed=0)

        duration = _get_duration(params.src)

        @ffmpeg.on("progress")
        def on_progress(progress: Progress):
            percentage = _get_progress_percentage(progress, duration)
            progress_bar.update(task, completed=percentage)

        @ffmpeg.on("completed")
        def on_completed():
            progress_bar.update(task, completed=100)

        @ffmpeg.on("stderr")
        def on_stderr(line):
            # This pattern checks for errors like "File 'input_compressed.mp4' already exists.".
            # Such errors may occur on Linux, even when using the "-n" flag with ffmpeg.
            pattern = Constants.FFMPEG_FILE_ALREADY_EXISTS_ERROR_PATTERN
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                progress_bar.update(task, completed=100)

        try:
            ffmpeg.execute()

            tmp.rename(dst)

            if params.delete_original:
                params.src.unlink(missing_ok=True)

        except FFmpegError as error:
            _rethrow_ffmpeg_error(error)

        finally:
            tmp.unlink(missing_ok=True)


@ffmpeg_required
def compress_videos_recursively(params: CompressParams) -> None:
    dst = params.dst if params.dst else params.default_dst

    if dst.suffix:
        raise Exception("Invalid argument: Output must be a directory")

    count = 0
    videos_count = 0

    for file in params.src.rglob("*"):
        if file.suffix.lower() in Constants.SUPPORTED_VIDEO_FORMATS:
            videos_count += 1

    for file in params.src.rglob("*"):
        if not file.is_file():
            continue

        relative_path = file.relative_to(params.src)
        output_file = dst / relative_path

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)

        if file.suffix.lower() in Constants.SUPPORTED_VIDEO_FORMATS:
            console.print(f"[{count} / {videos_count}] ", style="green", end="")
            compress_video(params.copy_with(src=file, dst=output_file))
            count += 1
        else:
            shutil.copy2(file, output_file)

    if params.delete_original:
        shutil.rmtree(params.src, ignore_errors=True)
