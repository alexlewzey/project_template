"""Common utility functions."""

from typing import Any


def to_list(o: Any) -> list:
    if isinstance(o, str):
        return [o]
    else:
        return list(o)
