from pathlib import Path

import pytest
from typer.testing import CliRunner

from vidpack.cli import app

runner = CliRunner()

PROGRESS_COMPLETION_OUTPUT = "100% 0:00:00"

TEST_VIDEOS_PATH: Path = Path(__file__).parent / "resources"
INPUT: str = str(TEST_VIDEOS_PATH / "sample_1.mp4")


def test_single_file_compression_with_wrong_path():
    result = runner.invoke(app, ["wrong_path.mp4"])
    expected_message = "INPUT path does not exists"
    assert result.exit_code == 0, result.stdout
    assert expected_message in result.stdout


def test_single_file_compression_with_default_options():
    result = runner.invoke(app, [INPUT])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


@pytest.mark.parametrize("codec", ["h264", "libx265"])
def test_single_file_compression(codec):
    result = runner.invoke(app, [INPUT, "--codec", codec])
    assert result.exit_code == 0, result.stdout
    assert PROGRESS_COMPLETION_OUTPUT in result.stdout


@pytest.mark.parametrize("codec", ["libx267", "123"])
def test_single_file_compression_with_invalid_codec(codec):
    result = runner.invoke(app, ["input.mp4", "--codec", codec])
    expected_message = f"Invalid value for '--codec' / '-c': '{codec}'"
    assert result.exit_code == 2, result.stdout
    assert expected_message in result.stdout, result.stdout
