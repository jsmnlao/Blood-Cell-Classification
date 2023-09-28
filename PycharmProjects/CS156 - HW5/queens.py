# ----------------------------------------------------------------------
# Name:     queens
# Purpose:  Homework 5
#
# Author(s): Jasmine Lao, Rachel Liao
#
# ----------------------------------------------------------------------
"""
N-queens puzzle solver implementation

btack:      basic backtracking search
btrackac3:  backtracking search with AC-3 as a preprocessing step
"""
import csp
import string

# Enter your helper functions here
def build_csp(n, q1):
    """
        Creates a Csp object representing the puzzle,
        with all the domains (keys are variable names and the values
        are sets representing their domains), variables, and constraints
        :param n: is the number of queens
        :param q1: the row position associated with the queen in column 1
        :return: a Csp object.
        """
    # Domain dictionary representing allowable domains for each queen
    domains = {}
    # Figure out values representing allowable domains
    values = set()
    for i in range(1, n+1):
        values.add(i)
    # Fill domain dictionary
    for index in range(1, n+1):
        domains[index] = values
    print("domains", domains)

    # Neighbors dictionary representing binary constraints
    neighbors = 0

    # Constraints function
    constraints = 0


    # csp_object = csp.Csp(domains, neighbors, constraints)


def constraint_function(var1, val1, var2, val2):
    """
    A function that takes as arguments two variables and two values and returns True
    if var1 and var2 satisfy the constraint when their respective values are val1 and val2.
    :param var1: variable 1 --> variable name/col
    :param val1: variable 1's value --> variable row
    :param var2: variable 2 --> variable name/col
    :param val2: variable 2's value --> variable row
    :return: true if satisfies constraints, false if violates constraints
    """
    # Queens on the same row
    if val1 == val2:
        return False
    # Queens on the same diagonal
    elif abs(val1 - val2) == 1:
        return False
    else:
        return True


def btrack(n, q1):
    """
    Solve the given puzzle with basic backtracking search
    :param n: is the number of queens
    :param q1: the row position associated with the queen in column 1
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    build_csp(n, q1)


def btrackac3(n, q1):
    """
    Solve the given puzzle with backtracking search and AC-3 as
    a preprocessing step.
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    pass