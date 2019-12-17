# standard library
import os
from pathlib import Path

# dependent packages
import toml

# constants
PATH = Path(os.environ["PROJECT_PATH"]) / "xarray"


def test_sdarray(filename="sdarray.toml"):
    with open(PATH / filename) as f:
        toml.load(f)
