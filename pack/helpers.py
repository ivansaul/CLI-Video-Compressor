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
