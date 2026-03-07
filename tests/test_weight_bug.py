# tests/test_weight_bug.py

import sys
import os
import pytest

# Ensure the parent folder (where app.py lives) is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import main_conversion_function

def test_pounds_to_kg_bug():
    value = 100
    expected = 45.3592  # correct kg value
    assert main_conversion_function(value, 'pounds', 'kg') == expected
