# *********************** #
# Erwin Medina - 10/15/24 #
# Leetcode #26 - Easy     #
# *********************** #
import pytest

# ***************************************************************************** #
# Directions: 
# Given an integer array nums sorted in non-decreasing order,
# Remove the duplicates in place, such that each unique element
# Only appears once. The relative order of the elements should be kept 
# The same. Return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted,
# You need to do the following:
    # Change the array nums such that the first k elements of nums contains
    # the unique elements in the order they were present in nums initially.
    # Remaining elements of nums are not important as well as the size of nums.
# Return k
# ***************************************************************************** #

# ************************ #
# Focus Points:
# Two pointer technique 
# ************************ #

def removeDuplicates(nums):

    # ******************************* #
    # Method 1 - O(n)                 #
    # ******************************* #
    current = nums[0]
    i = 1
    
    while i < len(nums):
        # If we've reached the underscore replacement, then return
        if current == "_": 
            return nums
        # If duplicate, remove and append underscore
        elif current == nums[i]: 
            nums.pop(i)
            nums.append("_")
        # If done, update current and move on
        else: 
            current = nums[i]
            i += 1

    return nums

    # ************************************************************************** #
    # Method 1 - Explanation
    # Initialize variables at nums[0] and a pointer for i
    # Iterate from i to the length of nums
    # If we've reached an underscore value, then we're done.
    # If we've reached a duplicate, remove it from list, append blank at the end
    # If neither, then increment our pointer and move on.
    # Finally, when all done, we return nums. 
    # Ideally, we should be returning the count of unique numbers.
    # ************************************************************************** #

# *********************************************************** #
# Created unit tests to simplify checking right/wrong answers #
# *********************************************************** #
def test_removeDuplicates():
    assert removeDuplicates([1,1,2]) == [1,2, "_"]
    assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4,"_","_","_","_","_"]

# ************************************************* #
# How to run the tests:
# python3 -m pytest LeetCode/Easy/Leetcode26_RemoveDuplicates.py
# ************************************************* #