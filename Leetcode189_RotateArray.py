# ************************ #
# Erwin Medina  - 10/15/24 #
# Leetcode #189 - Medium   #
# ************************ #
import pytest

# *********************************************************************** #
# Directions:
# Given an integer array nums, rotate the array to the right by k steps.
# Where k is a non-negative value.
# *********************************************************************** #

# *************************** #
# Focus Points:
# Array Manipulation, Slicing
# *************************** #

def rotateArray(nums, k):

    # ******************* #
    # Method 1 - O(k * n) #
    # ******************* #
    # i = 0
    # while i < k:
    #     storedValue = nums[-1]
    #     nums.pop()
    #     nums.insert(0,storedValue)
    #     i += 1
    # print(nums)
    # return nums

    # *************************************************************************************** #
    # Method 1 - Explanation
    # - Iterate from 1 to k
    # - Starting from the back, store the last value. Remove it from the list.
    # - Then insert it to the front.
    # - I know from CS that inserting to the front of the list is O(n) and not efficient.
    # - As it throws off all the indexes and the list has to 'create' a new list.
    # - This was my first attempt. Not very good. But it worked and passed LeetCode. Barely.
    # *************************************************************************************** #

    # *************** #
    # Method 2 - O(n) #
    # *************** #

    # Accounts if k is larger than nums length
    k = k % len(nums)

    # Function to Reverse the Array
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
    reverse(nums, 0, len(nums)-1)   # reverses entire array
    reverse(nums, 0, k - 1)         # reverses first k elements
    reverse(nums, k, len(nums)-1)   # reverses remaining elements.

rotateArray([1,2,3,4,5,6,7], 3)