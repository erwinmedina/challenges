# *********************** #
# Erwin Medina - 11/07/25 #
# Leetcode #13 - Easy     #
# *********************** #
import pytest

def longestCommonPrefix(strs: list[str]) -> str:
    # region - Attempt 1 #
    pointer = 0
    commonPrefix = ""
    shortestWordLength = len(min(strs, key=len))

    while pointer < shortestWordLength:
        wordMap = {}
        for word in strs:
            wordMap[word[pointer]] = wordMap.get(word[pointer], 0) + 1
        if wordMap[word[pointer]] == len(strs):
            commonPrefix += word[pointer]
        else:
            break
        pointer += 1
    print(commonPrefix)
    return commonPrefix
    #endregion 

    # region - Attempt 2 - Chatgpt Recommendation #
    # if not strs:
    #     return ""
    # shortest = min(strs, key=len)

    # for i in range(len(shortest)):
    #     char = strs[0][i]
    #     for word in strs:
    #         if word[i] != char:
    #             return shortest[:i]
        
    # return shortest



# *********************************************************** #
# Created unit tests to simplify checking right/wrong answers #
# *********************************************************** #
def test_longestCommonPrefix():
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix(["cir", "car"]) == "c"
    assert longestCommonPrefix(["racecar", "dog", "car"]) == ""

"""
How to run the tests:
python3 -m pytest LeetCode/Easy/Leetcode14_LongestCommonPrefix.py
"""

longestCommonPrefix(["flower", "flow", "flight"])
longestCommonPrefix(["racecar", "dog", "car"])
longestCommonPrefix(["cir", "car"])