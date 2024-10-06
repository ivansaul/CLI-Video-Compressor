import os
from pathlib import Path

from .constants import Constants


def list_unprocessed_videos(
    source: str,
    skip_suffix: str,
) -> list[str]:
    """
    Get a list of all unprocessed video files in a directory.

    Args:
        source (str): The path to the input directory.
        skip_suffix (str): The suffix to skip when checking for processed files.

    Returns:
        list[str]: A list of all unprocessed video files in the input directory.
    """
    videos: list[str] = []
    for root, _, files in os.walk(source):
        for file in files:
            if file.endswith(Constants.SUPPORTED_VIDEO_FORMATS):
                if not Path(file).stem.endswith(skip_suffix):
                    videos.append(os.path.join(root, file))
    return videos


def convert_quality_to_crf(quality: int) -> int:
    """
    Convert a quality level from range [0, 100] to a Constant Rate Factor (CRF)
    value in range [23, 51]. Lower values mean (lower quality, higher compression).
    Higher values mean (higher quality, lower compression).

    Args:
        quality (int): The quality level to convert.

    Returns:
        int: The CRF value.
    """
    c, q = 51 - 23, 100 - 0
    return int(51 - quality * (c / q))
