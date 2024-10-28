# ************************ #
# Erwin Medina - 10/28/24  #
# ChatGPT - Easy           #
# ************************ #
import pytest

# ************************************************************************ #
# Directions:
# ************************************************************************ #
# Square each element in a given list, using list comprehension

# ************** #
# Focus Points:
# ************** #

def squareNums(nums):

    # *************** #
    # Method 1 - O(n) #
    # *************** #
    return [x*x for x in nums]

    # ******************************************************************************** #
    # Explanation - Method 1 #
    # ******************************************************************************** #

squareNums([1,2,3,4])

def test_squareNums():
    assert squareNums([1,2,3,4]) == [1,4,9,16]
    assert squareNums([2,19,5,0]) == [4, 361, 25, 0]
    
# ************************************************************* #
# How to run the tests:
# python3 -m pytest ChatGPT/Easy/ListComprehension_SquareNums.py
# ************************************************************* #