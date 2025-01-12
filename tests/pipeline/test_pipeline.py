import os
import shutil
from argparse import Namespace
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

from src.pipeline.config import config
from src.pipeline.pipeline import run_pipeline



def test_run_pipeline():
    run_pipeline()
