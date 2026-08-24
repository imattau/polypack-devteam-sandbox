# tests/test_cli.py
import os
from pathlib import Path
from click.testing import CliRunner
from fsutil.cli import cli


def test_cli_list_command(tmp_path):
    """Ensure the `list` command returns the names of files in a directory."""
    # Create a few temporary files
    filenames = ["a.txt", "b.txt", "c.log"]
    for name in filenames:
        (tmp_path / name).write_text("test")

    runner = CliRunner()
    result = runner.invoke(cli, ["list", str(tmp_path)])
    # The command should exit successfully
    assert result.exit_code == 0
    output_lines = sorted(result.output.strip().splitlines())
    expected_lines = sorted(filenames)
    assert output_lines == expected_lines
