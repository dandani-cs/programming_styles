#!/usr/bin/env python3
import os
import re
import sys
from subprocess import getstatusoutput, getoutput

prg = "declared_intentions.py"
prg_wrong_str = "declared_intentions_wrong_str.py"
prg_wrong_list = "declared_intentions_wrong_list.py"
prg_wrong_dict = "declared_intentions_wrong_dict.py"

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
def test_wrong_str_type():
    """Checks if error is raised when expected str data type not given"""

    out = getoutput(f'python {prg_wrong_str} ../input_file.txt')

    assert "Expecting <class 'str'>, got " in out

# ----------------------------------------------------
def test_wrong_list_type():
    """Checks if error is raised when expected list data type not given"""

    out = getoutput(f'python {prg_wrong_list} ../input_file.txt')

    assert "Expecting <class 'list'>, got " in out

# ----------------------------------------------------
def test_wrong_dict_type():
    """Checks if error is raised when expected dict data type not given"""

    out = getoutput(f'python {prg_wrong_dict} ../input_file.txt')

    assert "Expecting <class 'dict'>, got " in out
