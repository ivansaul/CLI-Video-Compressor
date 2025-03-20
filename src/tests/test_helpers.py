from pathlib import Path

import pytest

from vidpack.helpers import add_affixes


@pytest.mark.parametrize(
    "target, prefix, suffix, expected_output",
    [
        (Path("/path/to/file.txt"), "", "", Path("/path/to/file.txt")),
        (Path("file.txt"), "prefix_", "", Path("prefix_file.txt")),
        (Path("/path/to/file.txt"), "", "_suffix", Path("/path/to/file_suffix.txt")),
        (Path("/file.txt"), "prefix_", "_suffix", Path("/prefix_file_suffix.txt")),
    ],
)
def test_add_affixes(target, prefix, suffix, expected_output):
    """
    Test add_affixes function with different combinations of prefix and suffix.
    """
    result = add_affixes(target=target, prefix=prefix, suffix=suffix)
    assert result == expected_output
