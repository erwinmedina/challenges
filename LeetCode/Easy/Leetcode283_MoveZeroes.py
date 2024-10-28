# ************************ #
# Erwin Medina  - 10/18/24 #
# Leetcode #283  - Easy    #
# ************************ #
import pytest

# ******************************************************************** #
# Directions:
# Given an integer array nums, move all 0's to the end while
# Maintaining the relative order of the non-zero elements
# Note: Do this in place without making a copy of the array
# ******************************************************************** #

# *************************************************** #
# Focus Points:
# Two pointer techniques, in place array manipulation
# *************************************************** #

def moveZeroes(nums):
    # ***************** #
    # Method 1 - O(n^2) #
    # ***************** #
    # region
    # i = 0
    # countZero = 0

    # while i < len(nums) - countZero:
    #     if nums[i] == 0:
    #         nums.pop(i)
    #         nums.append(0)
    #         countZero += 1
    #     else:
    #         i += 1
    # print(nums)
    # return nums

    # ************************************************************************** #
    # Explanation - Method 1
    # I thought this was a decent approach but it was O(n^2) because of the pop
    # Pop will shift all elements and change indexes, and cause a bottleneck
    # ************************************************************************** #
    # endregion

    # *************** #
    # Method 2 - O(n) #
    # *************** #
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for i in range(j, len(nums)):
        nums[i] = 0
    return nums

    # *********************************************************************************** #
    # Method 2 - Explanation
    # First for loop: we're seeing if a value is non zero, if it is, move it to the front.
    # The j counter is meant to keep track of 'the front' values.
    # Second for loop just replaces everything from j to the end with zeros
    # ez pz. Still couldn't nail it though.
    # *********************************************************************************** #

moveZeroes([0,1,0,3,12])

def test_moveZeroes():
    assert moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert moveZeroes([0]) == [0]

# ******************************************* #
# How to run the tests:
# python3 -m pytest LeetCode/Easy/Leetcode283_MoveZeroes.py
# ******************************************* #