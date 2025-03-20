from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from .constants import Constants
from .core import compress_video, compress_videos_recursively
from .helpers import try_except
from .models import CompressParams, VideoCodec

app = typer.Typer(rich_markup_mode="rich")


@app.command(epilog=Constants.EPILOG)
def main(
    input: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=True,
            show_default=False,
            help=Constants.INPUT_HELP_TEXT,
        ),
    ],
    output: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            show_default=True,
            help=Constants.OUTPUT_HELP_TEXT,
        ),
    ] = None,
    quality: Annotated[
        int,
        typer.Option(
            "--quality",
            "-q",
            min=0,
            max=100,
            clamp=True,
            show_default=True,
            help=Constants.QUALITY_HELP_TEXT,
        ),
    ] = 75,
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            "-w",
            show_default=True,
            help=Constants.OVERWRITE_HELP_TEXT,
        ),
    ] = False,
    delete_original: Annotated[
        bool,
        typer.Option(
            "--delete-original",
            "-d",
            help=Constants.DELETE_ORIGINAL_HELP_TEXT,
        ),
    ] = False,
    vcodec: Annotated[
        VideoCodec,
        typer.Option(
            "--codec",
            "-c",
            show_default=True,
            help=Constants.VIDEO_CODEC_HELP_TEXT,
        ),
    ] = VideoCodec.H264,
):
    """
    [green]Simple CLI app[/green] for compressing videos :sparkles:
    """

    params = CompressParams(
        src=input,
        dst=output,
        quality=quality,
        vcodec=vcodec,
        overwrite=overwrite,
        delete_original=delete_original,
    )

    _compress(params)


@try_except
def _compress(params: CompressParams) -> None:
    if params.src.is_file():
        compress_video(params)

    if params.src.is_dir():
        compress_videos_recursively(params)
