# ************************ #
# Erwin Medina - 10/23/24  #
# Leetcode #287 - Medium   #
# ************************ #
import pytest

# ************************************************************************ #
# Directions:
# ************************************************************************ #
# Given an array of integers nums containing n+1 integers where each integer
# is in the range [1,n] inclusive. There is only 1 repeated number in nums,
# Return this repeated number.
# Must solve without modifying the array nums and only using constant extra
# space. {Basically dont create a hash table}
# ************************************************************************ #

# ******************************************************* #
# Focus Points:
# Binary search and two pointer array [Tortoise and Hare]
# ******************************************************* #

def findDuplicate(nums):

    # *************** #
    # Method 1 - O(n) #
    # *************** #
    # dupeFound = False
    # firstP = 0
    # secondP = 1
    # numsLength = len(nums)

    # while not dupeFound:
    #     if nums[firstP] == nums[secondP] and firstP != secondP:
    #         return nums[firstP]
            
    #     else:
    #         secondP = (secondP + 2) % numsLength
    #         if nums[secondP] != nums[firstP]:
    #             firstP = (firstP + 1) % numsLength            

    # ********************************************************************************************* #
    # Explanation - Method 1 #
    # ********************************************************************************************* #
    # This approach apparently skips numbers. And for large sets might cause it to never find dupe.
    # I thought I was doing it the tortoise and hare way but i guess not :( 
    # ********************************************************************************************* # 

    # *************** #
    # Method 2 - O(n) #
    # *************** #
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast: # Finds intersection point
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    slow = 0
    while slow != fast: # Finds duplicate number
        slow = nums[slow]
        fast = nums[fast]

    return(slow)

    # ************************************************************************************* #
    # Explanation - Method 2
    # ************************************************************************************* #
    # Using tortoise and hare (slow/fast) we first try to find the intersection point. 
    # Of course, using nums[slow], and nums[nums[fast]] is confusing as an update value..
    # But because of the directions, we'll never be out of range. And eventually dupes are
    # Found. This is fast :(
    # ************************************************************************************* #

findDuplicate([4,3,1,4,2])

def test_findDuplicate():
    assert findDuplicate([4,3,1,4,2]) == 4
    assert findDuplicate([3,1,3,4,2]) == 3
    assert findDuplicate([3,3,3,3,3]) == 3
    return
    

# ************************************************* #
# How to run the tests:
# python3 -m pytest Leetcode287_FindDuplicateNumber.py
# ************************************************* #