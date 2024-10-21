# ************************ #
# Erwin Medina - 10/15/24  #
# Leetcode #217 - Easy     #
# ************************ #
import pytest

# ************************************************************************ #
# Directions:
# Given an integer array, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
# ************************************************************************ #

# ************** #
# Focus Points:
# Hash Tables
# ************** #

def containsDuplicates(nums):

    # *************** #
    # Method 1 - O(n) #
    # *************** #
    setNums = set(nums)
    if len(setNums) != len(nums):
        return False
    return True

    # ******************************************************************************** #
    # Explanation - Method 1 #
    # This creates a set (which only has unique values) from the num array provided.
    # Then it checks if the lengths are the same for both set and nums.
    # If they are, then great. Return true. Else, return false
    # Still O(n) but it can be improved because it still has to check the entire array
    # Before it can return a result. Unlike Method 2
    # ******************************************************************************** #

    # *************** #
    # Method 2 - O(n) #
    # *************** #
    hashTable = {}
    for i in nums:
        if i in hashTable:
            return True
        else:
            hashTable[i] = 1
    return False

    # ************************************************************************************* #
    # Explanation - Method 2
    # This creates a dictionary/hash table, where if it finds a number, add it to the hash
    # However, there's an "early exit" that says if it's already in the table, then just
    # Return true. This makes the code faster in case of duplicates happening early vs
    # Method 1 that checks the entire array (to get the length) before returning a result.
    # ************************************************************************************* #


containsDuplicates([1,2,3,4])

def test_ContainsDuplicates():
    assert containsDuplicates([1,2,3,1]) == True
    assert containsDuplicates([1,2,3,4]) == False
    assert containsDuplicates([1,1,1,3,3,4,3,2,4,2]) == True

# ************************************************* #
# How to run the tests:
# python3 -m pytest ContainsDuplicate_Leetcode217.py
# ************************************************* #