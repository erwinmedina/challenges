# *********************** #
# Erwin Medina - 11/06/25 #
# Leetcode #9 - Easy      #
# *********************** #
import pytest

"""
This is attempt 1. Apparently this method sorta sucks but I thought it was great.
Leetcode returned with a 20ms time. 
I thought my approach would reduce time since I have a pointer starting from the back
and if something doesn't match up along the way, it stops and returns.
but I guess "str(x) == str(x)[::-1]" is a better way to write it out.
"""

def isPalindrome(x: int) -> bool:
    """ ATTEMPT 1 """
    # region - attempt 1 #
    if x < 0: return False

    stringX = str(x)
    endPointer = len(stringX) - 1 # returns index

    for i in range(len(stringX)):
        print(stringX[i], stringX[endPointer], endPointer)
        if (stringX[i] == stringX[endPointer]):
            endPointer -= 1
            if endPointer < 0:
                return True
        else:
            return False
    #endregion
    
    """ ATTEMPT #2 """
    # region - attempt 2 #
    return str(x) == str(x)[::-1]
    # endregion


isPalindrome(121) # True
isPalindrome(-121) # False [121-]
isPalindrome(10) # False [01]

# *********************************************************** #
# Created unit tests to simplify checking right/wrong answers #
# *********************************************************** #
def test_isPalinedromeNumber():
    assert isPalindrome(121) == True
    assert isPalindrome(-121) == False
    assert isPalindrome(10) == False

"""
How to run the tests:
python3 -m pytest LeetCode/Easy/Leetcode9_PalindromeNumber.py

"""