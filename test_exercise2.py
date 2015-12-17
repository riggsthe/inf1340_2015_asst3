#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Farid Gassanov, Dusan Miletic, Tessie Riggs'
__email__ = "farid.gassanov@mail.utoronto.ca, dusan.miletic@utoronto.ca, tessie.riggs@gmail.com"
__copyright__ = "2015 Farid Gassanov, Dusan Miletic, Tessie Riggs"

__status__ = "Prototype"

# imports one per line
import pytest
import os
from exercise2 import *

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]
