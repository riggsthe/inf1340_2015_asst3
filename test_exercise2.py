#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

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

def test_quarantine():

    assert decide("test_quarantine.json","countries.json") == ["Quarantine"]

def test_visa():

    assert decide("test_visa.json","countries.json") == ["Reject"]

def test_country():

    assert decide("test_country.json","countries.json") == ["Reject"]
