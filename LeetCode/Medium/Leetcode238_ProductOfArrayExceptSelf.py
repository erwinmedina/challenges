# ************************ #
# Erwin Medina - 10/22/24  #
# Leetcode #238 - Medium   #
# ************************ #
import pytest
import math

# **************************************************************************** #
# Directions:
# Given an integer array nums, return an array "answer", such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32bit
# integer. Must be in O(n) time and without using division
# **************************************************************************** #

# ***************************************** #
# Focus Points:
# Prefix, suffix products without division
# ***************************************** #

def productOfArrayExceptSelf(nums):

    # ***************** #
    # Method 1 - O(n^2) #
    # ***************** #
    # productArray = []
    # for index, num in enumerate(nums):
    
    #     tempProd = 1
    #     if (index > 0):
    #         tempProd *= math.prod(nums[0:index])
    #     if (index < len(nums)):
    #         tempProd *= math.prod(nums[index+1:])
    #     productArray.append(tempProd)
    #     print(productArray)
    # return productArray

    # *********************************************************************************************************** #
    # Explanation - Method 1 #
    # I attempted to iterate through the index, and do some math.prod on all the values coming before and after.
    # This unfortunately leads to a O(n^2) time, which isn't ideal. So we go with method 2
    # *********************************************************************************************************** #

    # *************** #
    # Method 2 - O(n) #
    # *************** #
    numsLength = len(nums)
    left_products = [1] * numsLength
    right_products = [1] * numsLength
    result = [1] * numsLength

    # Calculates the left products
    for i in range(1, numsLength):
        left_products[i] = left_products[i-1] * nums[i-1]
    # Calculate the right products
    for i in range(numsLength-2, -1,-1):
        right_products[i] = right_products[i + 1] * nums[i+1]
    # Results
    for i in range(numsLength):
        result[i] = left_products[i] * right_products[i]
    return result

    # **************************************************************************** #
    # Explanation - Method 2 #
    # We initialize arrays with all 1's in them. 
    # Then we attempt to calculate the left products
    # Then we attempt to calculate the right products
    # Iterating once more, we multiply each of the arrays[i] to get our result.

    # This one was a bit confusing and hard to understand. 
    # Creating the left/right products seems ..weird. Will keep working on it.
    # **************************************************************************** #

productOfArrayExceptSelf([1,2,3,4])

def test_ProductOfArrayExceptSelf():
    assert productOfArrayExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productOfArrayExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

# ********************************************************* #
# How to run the tests:
# python3 -m pytest Leetcode238_ProductOfArrayExceptSelf.py
# ********************************************************* #