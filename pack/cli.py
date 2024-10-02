from typing import Optional

import typer
from rich import print
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
        print(f"[bold green] [Compressing...] {input}[/bold green]")
        compress_video(input_file=input, output_file=output, overwrite=overwrite)
    except Exception as e:
        error_message: str = Constants.ERROR_MESSAGE
        if debug:
            error_message += f"\n {e}"

        print(f"[bold red]{error_message}[/bold red]")
        raise typer.Exit()
