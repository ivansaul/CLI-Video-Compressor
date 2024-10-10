import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from vidpack.helpers import add_affixes, file_exists, is_ffmpeg_installed


@pytest.mark.parametrize(
    "file, prefix, suffix, expected_output",
    [
        (Path("/path/to/file.txt"), "", "", Path("/path/to/file.txt")),
        (Path("file.txt"), "prefix_", "", Path("prefix_file.txt")),
        (Path("/path/to/file.txt"), "", "_suffix", Path("/path/to/file_suffix.txt")),
        (Path("/file.txt"), "prefix_", "_suffix", Path("/prefix_file_suffix.txt")),
    ],
)
def test_add_affixes(file, prefix, suffix, expected_output):
    """
    Test add_affixes function with different combinations of prefix and suffix.
    """
    result = add_affixes(file=str(file), prefix=prefix, suffix=suffix)
    assert result == str(expected_output)


def test_ffmpeg_installed(monkeypatch):
    """
    Test that ffmpeg is installed by mocking subprocess.run.
    """

    # Simulate that ffmpeg is installed
    def mock_run(*args, **kwargs):
        return True

    monkeypatch.setattr(subprocess, "run", mock_run)
    assert is_ffmpeg_installed() is True


def test_ffmpeg_not_installed(monkeypatch):
    """
    Test that ffmpeg is not installed by mocking subprocess.run to raise FileNotFoundError.
    """

    # Simulate that ffmpeg is not installed
    def mock_run(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr(subprocess, "run", mock_run)

    assert is_ffmpeg_installed() is False


@patch("vidpack.helpers.Path.exists")
def test_file_exists(mock_exists):
    """
    Test file_exists function with different scenarios.
    """
    # Simulate that the file exists
    mock_exists.return_value = True
    assert file_exists("/path/to/existing_file.txt") is True

    # Simulate that the file does not exist
    mock_exists.return_value = False
    assert file_exists("/path/to/non_existent_file.txt") is False
