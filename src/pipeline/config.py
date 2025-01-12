"""Configuration management and validation."""

import os
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field



class Config(BaseModel):
    """Pipeline configuration with validation."""

    experiment_name: str

    model_config = ConfigDict(frozen=True)


def get_config() -> Config:
    """Load environment specific config conditional on environment variable."""
    env = os.environ.get("ENVIRONMENT", "dev")
    print(f"env: {env}")
    config_path = Path(__file__).parent.parent / "configs" / f"{env}.yaml"
    with config_path.open() as f:
        config_dict = yaml.safe_load(f)
    return Config(**config_dict)


config = get_config()
