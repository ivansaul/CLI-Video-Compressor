import os
from pathlib import Path

import pytest
from typer.testing import CliRunner

from vidpack.cli import app

runner = CliRunner()

PROGRESS_COMPLETION_OUTPUT = "100% 0:00:00"

TEST_VIDEOS_PATH: Path = Path(__file__).parent / "resources"
INPUT: str = str(TEST_VIDEOS_PATH / "sample_video_1.mp4")
INPUT_2: str = str(TEST_VIDEOS_PATH / "sample_video_2.mp4")
OUTPUT: str = str(TEST_VIDEOS_PATH / "output.mp4")
WRONG_INPUT: str = str(TEST_VIDEOS_PATH / "wrong_input.mp4")


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    """
    Fixture to setup and teardown the test environment.
    """
    yield
    for file in TEST_VIDEOS_PATH.glob("*_compressed.mp4"):
        os.remove(file)


def test_single_file_compression_with_default_options():
    """
    Test single file compression with default options.

    Expected results:
        - Exit code: 0
        - Progress completion output: "100% 0:00:00"
    """
    result = runner.invoke(app, [INPUT])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


@pytest.mark.parametrize("codec", ["h264", "libx265"])
def test_single_file_compression(codec):
    """
    Test single file compression with different video codecs.

    Expected results:
        - Exit code: 0
        - Progress completion output: "100% 0:00:00"
    """
    result = runner.invoke(app, [INPUT, "--codec", codec])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


@pytest.mark.parametrize("codec", ["libx267", "123"])
def test_single_file_compression_with_invalid_codec(codec):
    """
    Test single file compression with invalid video codec.

    Expected results:
        - Exit code: 2
    """
    result = runner.invoke(app, [INPUT, "--codec", codec])
    assert result.exit_code == 2, result.stdout


def test_single_file_compression_with_quality_option():
    """
    Test single file compression with quality option.

    Expected results:
        - Exit code: 0
        - Progress completion output: "100% 0:00:00"
    """
    result = runner.invoke(app, [INPUT, "--quality", "50"])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


def test_single_file_compression_with_overwrite_option():
    """
    Test single file compression with overwrite option.

    Expected results:
        - Exit code: 0
        - Progress completion output: "100% 0:00:00"
    """
    result = runner.invoke(app, [INPUT, "--overwrite"])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


def test_single_file_compression_with_delete_original_option():
    """
    Test single file compression with delete original option.

    Expected results:
        - Exit code: 0
        - Progress completion output: "100% 0:00:00"
    """
    result = runner.invoke(app, [INPUT_2, "--delete-original"])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


def test_single_file_compression_with_output_option():
    """
    Test single file compression with output option.

    Expected results:
        - Exit code: 0
        - Progress completion output: "100% 0:00:00"
    """
    result = runner.invoke(app, [INPUT, "--output", OUTPUT])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


def test_single_file_compression_with_wrong_path():
    """
    Test single file compression with wrong path.

    Expected results:
        - Exit code: 0
        - Error message: "INPUT path does not exists"
    """
    result = runner.invoke(app, [WRONG_INPUT])
    expected_message = "INPUT path does not exists"
    assert result.exit_code == 0, result.stdout
    assert expected_message in result.stdout
