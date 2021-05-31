#!/usr/bin/env python3
import os
import re
import sys
from subprocess import getstatusoutput, getoutput

prg = "plugins.py"
prg2 = "plugins2.py"

# --------------------------------------------------
def test_exists():
    """Checks if program exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_first_line():
    """Checks if output is correct for input_file.txt"""

    out = getoutput(f'python {prg} ../input_file.txt')
    expected = "2"

    assert out.split('\n')[0][-1] == expected

# ------------------------------------------------------
def test_sort():
    """Checks that the order of printing is from highest frequency to lowest"""

    out = getoutput(f'python {prg} ../input_file.txt')
    out.split('\n')

    basis = 'live - 2'
    to_find = 'africa - 1'

    assert to_find in out[out.index(basis) + 1:]

# ----------------------------------------------------
def test_config2():
    """Checks if the second version of modules works"""

    out = getoutput(f'python {prg} ../input_file.txt')
    expected = "2"

    assert out.split('\n')[0][-1] == expected

    basis = 'live - 2'
    to_find = 'africa - 1'

    assert to_find in out[out.index(basis) + 1:]
