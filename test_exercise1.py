#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS
Test module for exercise3.py
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise1 import selection, projection, cross_product


###########
# TABLES ##
###########


STUDENTS = [["FirstName", "Surname", "IQ", "GPA"],
             ["Hoban", "Washburne", 94, 3.2],
             ["Zoe", "Washburne", 110, 3.5],
             ["Malcolm", "Reynolds", 81, 2.6],
             ["Jayne", "Cobb", 55, 1.1],
             ["Inara", "Serra", 158, 4.0]]

STUDENTS_EMPTY = []

R1 = [["Student", "Class"],
      ["Zoe", "Programming"],
      ["Jayne", "Web Design"],
      ["Inara", "Programming"]]

R2 = [["Class", "Professor"],
      ["Programming", "Sim"],
      ["Web Design", "Yu"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):

    t1.sort()
    t2.sort()

    return t1 == t2


#####################
# FILTER FUNCTIONS ##
#####################
def filter_students(row):
    """
    Check if Student represented by row
    is AT LEAST 30 years old and makes
    MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 90 and row[-1] > 3.4


###################
# TEST FUNCTIONS ##
###################

def test_selection():
    """
    Test the selection operation.
    """

    result = [["FirstName", "Surname", "IQ", "GPA"],
              ["Zoe", "Washburne", 110, 3.5],
              ["Inara", "Serra", 158, 4.0]]

    assert is_equal(result, selection(STUDENTS, filter_students))


def test_selection_empty():
    assert selection(STUDENTS_EMPTY, filter_students) is\
        None


def test_project():
    """
    Test the projection operation.
    """

    result = [["FirstName", "Surname"],
              ["Hoban", "Washburne"],
              ["Zoe", "Washburne"],
              ["Malcolm", "Reynolds"],
              ["Jayne", "Cobb"],
              ["Inara", "Serra"]]

    assert is_equal(result, projection(STUDENTS, ["FirstName", "Surname"]))

def test_project_unknown_attribute_exception():

    try:
        project(STUDENTS, ["Does_Not_Exist"])
    except UnknownAttributeException:
        assert True



def test_cross_product():
    """
    Test cross product operation.
    """

    result = [["Student", "Class", "Class", "Professor"],
              ["Zoe", "Programming", "Programming", "Sim"],
              ["Zoe", "Programming", "Web Design", "Yu"],
              ["Jayne", "Web Design", "Web Design", "Yu"],
              ["Jayne", "Web Design", "Programming", "Sim"],
              ["Inara", "Programming", "Programming", "Sim"],
              ["Inara", "Programming", "Web Design", "Yu"]]

    assert is_equal(result, cross_product(R1, R2))