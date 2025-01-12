"""Common utility functions."""

from pathlib import Path
from typing import Any

import pandas as pd


def to_list(o: Any) -> None:
    if isinstance(o, str):
        return [o]
    else:
        return list(o)