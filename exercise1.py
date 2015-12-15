#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS
This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

####################
###  TABLES      ###
###################
STUDENTS = [["First Name", "Surname", "IQ", "GPA"],
           ["Hoban", "Washburne", 94, 3.2],
           ["Zoe", "Washburne", 110, 3.5],
           ["Malcolm", "Reynolds", 81, 2.6],
           ["Jayne", "Cobb", 55, 1.1],
           ["Inara", "Serra", 158, 4.0]]

R1 = [["Student", "Class"],
    ["Zoe", "Programming"],
    ["Jayne", "Web Design"],
    ["Inara", "Programming"]]

R2 =  [["Class", "Professor"],
    ["Programming", "Sim"],
    ["Web Design", "Yu"]]


#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def filter_students(row):
    """
    check if student represented by row has an IQ
    of at least 90 and a GPA of more than 3.4
    :param row: A List in the format:
    [{First name}, {Surname}, {IQ}, {GPA}]
    :return: True if the row satisfies the
    condition.
    return row[-2] >= 90 and row[-1] > 3.4
    """
    return row[-2] >= 90 and row[-1] > 3.4


def selection(t, f):
    
    """
    Perform select operation on table t that satisfy condition f.
    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]
    """
    select_table = []

    for row in t:
        # Check table row satisfies function then add to created table
        if f(row) is True:
            select_table.append(row)
        else:
            print "None"
            continue

    return select_table

# Selection (STUDENTS, filter_students)


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.
    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]
    """

    project_table = []
    location = []
    # find attribute location
    for item in range(len(r)):
        search = r[item]
        for i in range(len(t[0])):
            title = t[0][i]
            if search == title:
                location.append(i)
    if len(location) == 0:
        raise UnknownAttributeException

    # Now create a new array for each line on the table
    for i in range(len(t)):
        single_lines =[]
        line = t[i]
        for j in range(len(location)):
            index_local = location[j]
            info_to_grab = line[index_local]
            single_lines.append(info_to_grab)
        project_table.append(single_lines)

    return project_table

    # Projection (STUDENTS, ["First Name", "Surname"])
    

def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.
    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]
    """
    # First check lists to determine if any list is empty
    if len(t1) and len(t2) == 0:
        print "None"

    else:

        # Combine the headings of the table
        column_heads = t1[0]+t2[0]
        cross_table = []

        # Remove table headings
        del t1[0]
        del t2[0]

        return cross_table

