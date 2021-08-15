#!/usr/bin/env python3
import os
import re
import sys
from subprocess import getstatusoutput, getoutput
from subprocess import run as subprocessrun

prg = "lazy_rivers.py"

# --------------------------------------------------
def test_exists():
    """Checks if program exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_first_line():
    """Checks if output is correct for input_file.txt"""

    out = getoutput(f'python {prg} ../input_file.txt')
    expected = "2"

    assert out.split('\n')[1][-1] == expected

# ------------------------------------------------------
def test_sort():
    """Checks that the order of printing is from highest frequency to lowest"""

    out = getoutput(f'python {prg} ../input_file.txt')
    out.split('\n')

    basis = 'live - 2'
    to_find = 'africa - 1'

    assert to_find in out[out.index(basis) + 1:]
