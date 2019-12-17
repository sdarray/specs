# standard library
import os
from pathlib import Path

# dependent packages
import toml

# constants
PATH = Path(os.environ["PROJECT_PATH"]) / "xarray"
KEYS_REQUIRED = {"dtype", "default", "required", "doc"}
KEYS_OPTIONAL = {"dims", "option"}


def test_sdarray(filename="sdarray.toml"):
    with open(PATH / filename) as f:
        specs = toml.load(f)

    for item in specs.values():
        keys = set(item.keys())
        assert KEYS_REQUIRED <= keys
        assert (keys - KEYS_REQUIRED) <= KEYS_OPTIONAL
