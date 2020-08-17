#!/usr/bin/env python3
import os
import re
from subprocess import getstatusoutput, getoutput

prg = ".\\go_forth.py"

# --------------------------------------------------
def test_exists():
    """Checks if program exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_input_file():
    """Checks if output is correct for input_file.txt"""

    out = getoutput(f'{prg} ..\\input_file.txt')
    expected = """mostly - 2
live - 2
africa - 1
lions - 1
wild - 1
india - 1
tigers - 1
white - 1"""
    assert out.strip() == expected
