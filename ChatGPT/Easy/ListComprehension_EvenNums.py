# ************************ #
# Erwin Medina - 10/28/24  #
# ChatGPT - Easy           #
# ************************ #
import pytest

# ************************************************************************ #
# Directions:
# ************************************************************************ #
# Generate list of even numbers from 1 to 20 using list comprehension.

# ************** #
# Focus Points:
# ************** #

def squareNums(start, end):

    # *************** #
    # Method 1 - O(n) #
    # *************** #
    return [x for x in range(start,end+1) if x % 2 == 0]

    # ******************************************************************************** #
    # Explanation - Method 1 #
    # ******************************************************************************** #

squareNums(5, 9)

def test_squareNums():
    assert squareNums(10,20) == [10,12,14,16,18,20]
    assert squareNums(1,10) == [2,4,6,8,10]
    
# ************************************************************* #
# How to run the tests:
# python3 -m pytest ChatGPT/Easy/ListComprehension_EvenNums.py
# ************************************************************* #