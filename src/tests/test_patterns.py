import re

import pytest

from vidpack.constants import Constants


@pytest.mark.parametrize(
    "message, expected_match",
    [
        ("File 'input_compressed.mp4' already exists.", True),
        (
            "An error occurred: File 'input_compressed.mp4' already exists and cannot be overwritten.",
            True,
        ),
        ("Error: File 'input_compressed.mp4' already exists. Exiting.", True),
        ("Warning: File output.mp4 already exists. Please check.", True),
        ("Warning:fileOutput.mp4already exists.Please check.", True),
        ("The process completed successfully.", False),
        ("File 'input_compressed.mp4' is in use.", False),
        ("Error: Unable to open file 'input.mp4'.", False),
    ],
)
def test_ffmpeg_file_already_exists_error_pattern(message, expected_match):
    """
    Test the FFmpeg file already exists error pattern.
    """
    pattern = Constants.FFMPEG_FILE_ALREADY_EXISTS_ERROR_PATTERN
    match = re.search(pattern, message, re.IGNORECASE)
    assert (match is not None) == expected_match
