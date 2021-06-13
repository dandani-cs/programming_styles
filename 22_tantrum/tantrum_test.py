#!/usr/bin/env python3
import os
import re
import sys
from subprocess import getstatusoutput, getoutput

prg = "tantrum.py"
prg_stop = "tantrum_stop.py"

# --------------------------------------------------
def test_exists():
    """Checks if program exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_first_line():
    """Checks if output is correct for input_file.txt"""

    out = getoutput(f'python {prg} ../input_file.txt')

    assert "Less than 25 words!" in out

# -----------------------------------------------------
def test_IOError():
    """Checks that an IOError is raised when input file does not exist"""

    out = getoutput(f'python {prg}')

    assert "There is no input file!" in out


# -----------------------------------------------------
def test_stop_words_IOError():
    """Checks that the program raises an IO error when stop_words file not found"""

    out = getoutput(f'python {prg_stop} ../pride_and_prejudice.txt')

    assert "when opening ../stop_words.txt:" in out


# ----------------------------------------------------
def test_pride_first_line():
    """Checks if program outputs most frequent word"""

    out = getoutput(f'python {prg} ../pride_and_prejudice.txt')
    expected = "6"

    assert out.split('\n')[0][-1] == expected

# ---------------------------------------------------
def test_pride_sort():
    """Checks if program sort is working"""

    out = getoutput(f'python {prg} ../pride_and_prejudice.txt')
    basis = "mr - 786"
    to_find = "elizabeth - 635"

    assert to_find in out[out.index(basis) + 1:]
