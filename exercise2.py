#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia
Computer-based immigration office for Kanadia
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import re
import datetime
import json

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None

input_file = 'json/visitor_record.json'
countries_file = 'json/country_record.json'

with open(input_file,'r') as visitor_reader:
    visitor_info = visitor_reader.read()
    visitor_record = json.loads(visitor_info)


with open(countries_file,'r') as country_reader:
    country_info = country_reader.read()
    country_record = json.loads(country_info)



#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.
    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return (date - x_years_ago).total_seconds() < 0


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile(r'\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w-\w\w\w\w\w')
    passport_valid = passport_format.match(passport_number)
    if passport_valid is None:
        return False
    else:
        return True


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    date_format = re.compile(r'\d\d\d\d-\d\d-\d\d')
    date_valid = date_format.match(date_string)
    if date_valid is None:
        return False
    else:
        return True

def valid_form(visitor):
    for visitor in visitor_record:
        visitor_values = []
        for field_value in REQUIRED_FIELDS:
            if field_value in visitor.keys():
                visitor_values.append(field_value)

        if visitor_values != REQUIRED_FIELDS:
            return False
        else:
            return True

def valid_passport_and_date(visitor,country_record):
    if valid_passport_format(visitor["passport"]) and valid_date_format(visitor["birth_date"]):
        return True
    else:
        return False

def valid_visa(visitor, country_record):
    if visitor["home"]["country"] in country_record.keys():
        country_code = visitor["home"]["country"]
        if country_record[country_code]["visitor_visa_required"] == 1:
            return True
        else:
            return False

def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    visa_format = re.compile(r'\w\w\w\w\w-\w\w\w\w\w')
    visa_valid = visa_format.match(visa_code)
    if visa_valid is None:
        return False
    else:
        return True

def visa_expiration(date_string):

    now = datetime.datetime.now()
    two = now.replace(year=now.year - 2)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return (date - two).total_seconds() < 0


def valid_country(visitor, country_record):
    if visitor["home"]["country"] in country_record.keys() and visitor["from"]["country"] in country_record.keys():
        return True
    else:
        return False


def valid_health(visitor,country_record):
    if visitor["from"]["country"] in country_record.keys():
        if country_record[visitor["from"]["country"]]["medical_advisory"] != "":
            return True
        else:
            return False
    else:
        return True


def valid_reason(visitor,country_record):
    if visitor["entry_reason"] == "visit":
        visa_required = valid_visa(visitor,country_record)
        if visa_required == 1:
            return True
        else:
            return False


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted
    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
    decision = []

    for visitor in visitor_record:
        if not valid_form or not valid_passport_and_date:
            decision.append("Reject")

        else:

            advisory = valid_health(visitor,country_record)
            if advisory is True:
                decision.append("Quarantine")

            good_passport = valid_passport_format(visitor["passport"])
            if good_passport is False:
                decision.append("Reject")

            known_locations = valid_country(visitor,country_record)
            if visitor["home"]["country"] != "KAN" and known_locations is False:
                decision.append("Reject")

            elif visitor["home"]["country"] == "KAN":
                decision.append("Accept")
            else:
                purpose_of_visit = valid_reason(visitor,country_record)
                if purpose_of_visit:
                    if valid_date_format(visitor["visa"]["date"]):
                        if visa_expiration(visitor["visa"]["date"]):
                            decision.append("Reject")

    print decision


decide(input_file, countries_file)