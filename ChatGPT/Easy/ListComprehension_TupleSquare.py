# ************************ #
# Erwin Medina - 10/28/24  #
# ChatGPT - Easy           #
# ************************ #
import pytest

# ************************************************************************ #
# Directions:
# ************************************************************************ #
# Create a list of tuples where each tuple contains a number and its square.

# ************** #
# Focus Points:
# ************** #

def tupleSquare(start, end):

    # *************** #
    # Method 1 - O(n) #
    # *************** #
    return [(x,x*x) for x in range(start,end+1)]

    # ******************************************************************************** #
    # Explanation - Method 1 #
    # ******************************************************************************** #

tupleSquare(1, 4)

def test_tupleSquare():
    assert tupleSquare(1,4) == [(1,1), (2,4), (3,9), (4,16)]
    
# ************************************************************* #
# How to run the tests:
# python3 -m pytest ChatGPT/Easy/ListComprehension_TupleSquare.py
# ************************************************************* #