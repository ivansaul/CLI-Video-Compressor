from typing import Optional

import typer
from ffmpeg import FFmpegError  # type: ignore
from rich import print
from rich.markup import escape
from typing_extensions import Annotated

from .constants import Constants
from .helpers import is_ffmpeg_installed
from .utils import compress_video

app = typer.Typer(rich_markup_mode="rich")


@app.command(epilog=Constants.EPILOG)
def main(
    input: Annotated[
        str,
        typer.Argument(
            show_default=False,
            help=Constants.INPUT_HELP_TEXT,
        ),
    ],
    output: Annotated[
        Optional[str],
        typer.Option(
            show_default=True,
            help=Constants.OUTPUT_HELP_TEXT,
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        typer.Option(
            show_default=True,
            help=Constants.OVERWRITE_HELP_TEXT,
        ),
    ] = False,
    debug: Annotated[
        bool,
        typer.Option(
            help=Constants.DEBUG_HELP_TEXT,
            rich_help_panel=Constants.UTILS_PANEL_TEXT,
        ),
    ] = False,
):
    """
    [green]Simple CLI app[/green] for compressing videos :sparkles:
    """

    if not is_ffmpeg_installed():
        print(Constants.FFMPEG_NOT_INSTALLED)
        raise typer.Exit()

    try:
        print("[green]⠹ Processing...[/green]")
        print(f"[green]{escape(f'[{input}]')}[/green]")
        compress_video(input_file=input, output_file=output, overwrite=overwrite)
    except FFmpegError as e:
        ffmpeg_error_message: str = e.message
        if debug:
            ffmpeg_error_message += f"\n{e.arguments}"
        print(f"[bold red]{ffmpeg_error_message}[/bold red]")
    except Exception as e:
        unknown_error_message: str = Constants.UNKNOWN_ERROR_MESSAGE
        if debug:
            unknown_error_message += f"\n{e}"
        print(f"[bold red]{unknown_error_message}[/bold red]")
    else:
        raise typer.Exit()
