import subprocess

import pytest

from pack.helpers import add_affixes, is_ffmpeg_installed


@pytest.mark.parametrize(
    "file, prefix, suffix, expected_output",
    [
        ("/path/to/file.txt", "", "", "/path/to/file.txt"),
        ("file.txt", "prefix_", "", "prefix_file.txt"),
        ("/path/to/file.txt", "", "_suffix", "/path/to/file_suffix.txt"),
        ("/file.txt", "prefix_", "_suffix", "/prefix_file_suffix.txt"),
    ],
)
def test_add_affixes(file, prefix, suffix, expected_output):
    """
    Test add_affixes function with different combinations of prefix and suffix.
    """

    result = add_affixes(file=file, prefix=prefix, suffix=suffix)
    assert result == expected_output


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
