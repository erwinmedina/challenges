# ************************ #
# Erwin Medina  - 10/17/24 #
# Leetcode #53  - Medium   #
# ************************ #
import pytest

# ******************************************************************** #
# Directions:
# Given an integer array nums, find the subarray with the largest sum,
# Return its sum
# ******************************************************************** #

# ****************************************** #
# Focus Points:
# Dynamic Programming, Manipulating Subarray
# ****************************************** #

def maximumSubarray(nums):

    # *************** #
    # Method 1 - O(n) #
    # *************** #
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

    # *********************************************************** #
    # Explanation - Method 1                                      #
    # - Initialize the current sum and max sum
    # - Iterate through entire nums list
    # - Determine the maximum between num and (current_sum + num)
        # - This updates current subarray or starts a new one
    # - Determine the max between max_sum and current_sum
        # - Update max_sum if current_sum is greater.
    # *********************************************************** #

maximumSubarray([5,4,-1,7,8])

def test_maximumSubarray():
    assert maximumSubarray([5,4,-1,7,8]) == 23
    assert maximumSubarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maximumSubarray([1]) == 1

# *********************************************** #
# How to run the tests:
# python3 -m pytest MaximumSubarray_Leetcode53.py
# *********************************************** #