"""Initialization code that is run whenever the DrivingLogger package is
imported. Creates base references to things.

__author__: Nick Vazquez (nmv)
__created__: 2022/03/30
"""
import os
import pathlib

os.environ['UPDATE_INTERVAL_MS'] = '100'
os.environ['BASE_DIR'] = str(pathlib.Path(__file__).parent)
