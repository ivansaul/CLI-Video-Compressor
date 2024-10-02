from ffmpeg_progress_yield import FfmpegProgress
from rich.console import Console
from rich.progress import Progress

from .helpers import add_affixes, file_exists


def compress_video(
    input_file: str,
    output_file: str | None,
    overwrite: bool = False,
):
    """
    Compress a video file using FFmpeg and display the progress in a terminal.

    Args:
        input_file (str): The path to the input video file.
        output_file (str | None): The path to the output file. If not provided,
                                  a suffix '_compressed' will be added to the input file name.
        overwrite (bool): If True, overwrites the output file if it already exists.
                         If False, the process will stop if the output file exists.
    """

    if output := output_file:
        pass
    else:
        output = add_affixes(input_file, suffix="_compressed")

    if file_exists(output) and not overwrite:
        console = Console()
        console.print(
            f" [Skipped][{output}][Already exists]",
            style="bold green",
            markup=False,
        )
        return

    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-vcodec",
        "h264",
        "-acodec",
        "aac",
        output,
        "-y" if overwrite else "-n",
    ]

    process = FfmpegProgress(command)
    with Progress() as progress_bar:
        task = progress_bar.add_task("", total=100, completed=0)
        for progress in process.run_command_with_progress():
            progress_bar.update(task, completed=progress)
