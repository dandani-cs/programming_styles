#!/usr/bin/env python3
import os
import re
import sys
from subprocess import getstatusoutput, getoutput
from subprocess import run as subprocessrun

prg = "persistent_tables.py"

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

# ---------------------------------------------------
def test_db_file_exists():
    """Checks if database file was created"""

    assert os.path.isfile("tf.db")

# ---------------------------------------------------
def test_db_tables():
    """Checks if correct database tables was created"""

    command = "sqlite3; .open tf.db; .tables";

    ret = subprocessrun(command, capture_output=True, shell=True)

    out = ret.stdout.decode()

    assert "documents" in out
    assert "words" in out
    assert "characters" in out
