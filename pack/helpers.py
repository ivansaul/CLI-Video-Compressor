import shutil
import subprocess
from pathlib import Path


def is_ffmpeg_installed() -> bool:
    """
    Check if ffmpeg is installed.

    Returns:
        bool: True if ffmpeg is installed, False otherwise.
    """
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except FileNotFoundError:
        return False


def add_affixes(file: str, prefix: str = "", suffix: str = "") -> str:
    """
    Add a prefix and suffix to a file path, preserving the file extension.

    Args:
        file (str): The original file path.
        prefix (str): The prefix to add before the file name (default is an empty string).
        suffix (str): The suffix to add before the file extension (default is an empty string).

    Returns:
        str: The new file path with the prefix and suffix added.

    Example:
        /path/to/file.mp4 -> /path/to/prefix_file_suffix.mp4
    """
    path = Path(file)
    new_file_name = f"{prefix}{path.stem}{suffix}{path.suffix}"
    return str(path.with_name(new_file_name))


def file_exists(file: str) -> bool:
    """
    Check if a file exists.

    Args:
        file (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return Path(file).exists()


def is_file(path: str) -> bool:
    """
    Check if a path is a file.

    Args:
        path (str): The path to the file.

    Returns:
        bool: True if the path is a file, False otherwise.
    """
    return Path(path).is_file()


def is_dir(path: str) -> bool:
    """
    Check if a path is a directory.

    Args:
        path (str): The path to the directory.

    Returns:
        bool: True if the path is a directory, False otherwise.
    """
    return Path(path).is_dir()


def delete_path(path: str) -> None:
    """
    Delete a file or folder. If the path is a directory, it will be deleted recursively.
    If the path does not exist, it will be silently ignored.

    Args:
        path (str): The path to the file or folder.
    """
    target = Path(path)
    if target.exists():
        if target.is_file():
            target.unlink()
        elif target.is_dir():
            shutil.rmtree(target)
