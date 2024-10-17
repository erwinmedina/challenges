# *********************** #
# Erwin Medina - 10/15/24 #
# Leetcode #1 - Easy      #
# *********************** #
import pytest

def TwoSum(nums, target):
    # ********************************************************************** #
    # Directions:                                                           
    # Given an array of integers, and an int, 
    # return indices of the two numbers such that they add up to the target.
    # Return can be in any order.
    # ********************************************************************** #

    # *********************************************** #
    # Focus Points:
    # Array traversal, hash tables (dictionaries)
    # *********************************************** #

    # ********************************* #
    # Example:          
    # nums = [2,7,11,15], target = 9
    # output = [0,1]
    # reasoning = nums[0] + nums[1] = 9
    # ********************************* #

    # ****************** #
    # Method 1 - O(n^2)  #
    # ****************** #
    # returnArray = []
    # for i in range(len(nums)-1):
    #     for j in range(1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             returnArray.append(i)
    #             returnArray.append(j)
    #             print(returnArray)
    #             return returnArray

    # ****************************************************************** #
    # Method 1 - Explanation
    # This is the not so good way of doing it. Time complexity is high.
    # Double for loop does get the job done but its not efficient.
    # ****************************************************************** #
            
    # ****************** #
    # Method 2 - O(n)    #
    # ****************** #
    number_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in number_map:
            return [number_map[complement], i]
        number_map[num] = i

    # ****************************************************************** #
    # Method 2 - Explanation 
    # Here we're using the following key concepts:
        # enumerate
        # complement
        # dictionary
    # Enumerate allows us to keep track of index, and value we're on.
    # Complement helps us from using a second iterator
    # Dictionary helps keeping track of values we've already seen.
    # ****************************************************************** #

# *********************************************************** #
# Created unit tests to simplify checking right/wrong answers #
# *********************************************************** #
def test_TwoSums():
    assert TwoSum([2,7,11,15], 9) == [0,1]
    assert TwoSum([3,2,4], 6) == [1,2]
    assert TwoSum([3,3], 6) == [0,1]

# ************************************* #
# How to run the tests:
# python3 -m pytest TwoSum_Leetcode1.py
# ************************************* #