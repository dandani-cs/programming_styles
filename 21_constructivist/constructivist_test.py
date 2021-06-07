#!/usr/bin/env python3
import os
import re
import sys
from subprocess import getstatusoutput, getoutput

prg = "constructivist.py"

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

# -----------------------------------------------------
def test_IOError():
    """Checks that an IOError is raised when input file does not exist"""

    out = getoutput(f'python {prg} ../input_file.txt')

    assert "I/O error" in out


# -----------------------------------------------------
def test_stop_words_IOError(tmp_path):
    """Checks that the program raises an IO error when stop_words file not found"""

    out = getoutput(f'python {prg} ../input_file.txt')

    assert "when opening ../stop_words.txt:" in out
