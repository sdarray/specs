# standard library
from pathlib import Path

# dependent packages
import toml

# constants
DIR_PATH = Path("xarray")
KEYS_REQUIRED = {"dtype", "default", "required", "doc"}
KEYS_OPTIONAL = {"dims", "option"}


def test_sdarray(filename="sdarray.toml"):
    with open(DIR_PATH / filename) as f:
        specs = toml.load(f)

    for info in specs.values():
        keys = set(info.keys())
        assert KEYS_REQUIRED <= keys
        assert (keys - KEYS_REQUIRED) <= KEYS_OPTIONAL
