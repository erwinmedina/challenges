# ************************ #
# Erwin Medina - 10/24/24  #
# Leetcode #704 - Easy     #
# ************************ #
import pytest

# ************************************************************************ #
# Directions:
# ************************************************************************ #
# Given an array of integers nums which is sorted in ascending order, and an 
# integer target, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
# Algorithm must run in O(log n).
# ************************************************************************ #

# *************************************** #
# Focus Points:
# Divide and Conquer, Recursion/Iteration
# *************************************** #

def binarySearch(nums, target):

    # *************** #
    # Method 1 - O(n) #
    # *************** #
    
    tempIndex = 0

    if nums[0] == target:
        return 0
    
    while len(nums) > 1:
        midValue = len(nums) // 2
        if nums[midValue] == target:
            return tempIndex + midValue
        
        elif nums[midValue] > target:
            nums = nums[0:midValue]
        
        elif nums[midValue] < target:
            nums = nums[midValue:]
            tempIndex += midValue
    
    return -1

    # ******************************************************************************** #
    # Explanation - Method 1 #
    # ******************************************************************************** #
    # So here we're taking a binary search approach. Straight forward.
    # Edge Condition: If the nums array is just 1 and we find our target, return index 0.
    # Else, it'll start cutting the array in half at see which half it needs to further
    # Look at. Repeats until it finds it.
    # I created a tempIndex to track the actual index when we cut the array in half
    # and only analyze the right side. It helped. Woot.
    # This approach is O(log n) and meets the criteria. Yay
    # ******************************************************************************** #

binarySearch([-1, 0, 3, 5, 9, 12], 9)

def test_binarySearch():
    assert binarySearch([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binarySearch([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binarySearch([5], 5) == 0
    
# ************************************************* #
# How to run the tests:
# python3 -m pytest Leetcode704_BinarySearch.py
# ************************************************* #