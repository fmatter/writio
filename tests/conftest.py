"""Tests for the writio module.
"""
import pytest
import pathlib


@pytest.fixture
def data():
    return pathlib.Path(__file__).parent / "data"
