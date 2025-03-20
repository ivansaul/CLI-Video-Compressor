import shutil
from functools import wraps
from pathlib import Path
from typing import Any, Callable

from rich import box, print
from rich.panel import Panel


def ffmpeg_required(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if not shutil.which("ffmpeg"):
            raise Exception("ffmpeg is not installed")
        return func(*args, **kwargs)

    return wrapper


def try_except(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            panel = Panel(
                f"{e}",
                title="[red]Error[/red]",
                border_style="red",
                title_align="left",
                box=box.ROUNDED,
                expand=False,
            )
            print(panel)

    return wrapper


def add_affixes(target: str | Path, prefix: str = "", suffix: str = "") -> Path:
    """
    Add a prefix and suffix to a target path, preserving the file extension.

    Args:
        target (str | Path): The original target path.
        prefix (str): The prefix to add before the target (default: "").
        suffix (str): The suffix to add before the target (default: "").

    Returns:
        str: The new target path with the prefix and suffix added.

    Example:
        /path/to/file.mp4 -> /path/to/prefix_file_suffix.mp4
        /path/to/dir -> /path/to/prefix_dir_suffix
    """
    path = target if isinstance(target, Path) else Path(target)
    new_file_name = f"{prefix}{path.stem}{suffix}{path.suffix}"
    return path.with_name(new_file_name)
