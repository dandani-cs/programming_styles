#!/usr/bin/env python3
import os
import re
from subprocess import getstatusoutput, getoutput

prg = ".\\old_times_ex2.py"

# --------------------------------------------------
def test_exists():
    """Checks if program exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_input_file():
    """Checks if output is correct for input_file.txt"""

    out = getoutput(f'{prg} ..\\input_file.txt')
    expected = """live - 2
mostly - 2
white - 1
tigers - 1
india - 1
wild - 1
lions - 1
africa - 1"""
    assert out.strip() == expected
