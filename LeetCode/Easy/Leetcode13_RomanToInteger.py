# *********************** #
# Erwin Medina - 11/06/25 #
# Leetcode #13 - Easy     #
# *********************** #
import pytest

def romanToInt(s: str) -> int:
    """ Attempt 1 """
    # region - Attempt 1 #

    # romanNumerals = {
    #     "I": 1,
    #     "IV": 4,
    #     "V": 5,
    #     "IX": 9,
    #     "X": 10,
    #     "XL": 40,
    #     "L": 50,
    #     "XC": 90,
    #     "C": 100,
    #     "CD": 400,
    #     "D": 500,
    #     "CM": 900,
    #     "M": 1000,
    # }

    # counter = 0
    # i = 0

    # while i <= len(s) - 1:
    #     if (i != len(s) - 1):
    #         if (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")):
    #             counter += romanNumerals[s[i] + s[i+1]]
    #             i += 1
    #         elif (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")):
    #             counter += romanNumerals[s[i] + s[i+1]]
    #             i += 1
    #         elif (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M")):
    #             counter += romanNumerals[s[i] + s[i+1]]
    #             i += 1
    #         else:
    #             counter += romanNumerals[s[i]]
    #     else:
    #         counter += romanNumerals[s[i]]
    #     i += 1
    # return counter
    # endregion #

    """ Attempt 2 """
    # region - Attempt 2 - Chatgpt Recommendation #
    romanNumerals = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100,
        "D": 500, "M": 1000,
    }
    total = 0
    i = 0

    while i < len(s):
        if (i + 1 < len(s)) and (romanNumerals[s[i]] < romanNumerals[s[i+1]]):
            total += romanNumerals[s[i+1]] - romanNumerals[s[i]]
            i += 2
        else:
            total += romanNumerals[s[i]]
            i += 1
    return total

# *********************************************************** #
# Created unit tests to simplify checking right/wrong answers #
# *********************************************************** #
def test_romanToInt():
    assert romanToInt("III") == 3
    assert romanToInt("LVIII") == 58
    assert romanToInt("MCMXCIV") == 1994

"""
How to run the tests:
python3 -m pytest LeetCode/Easy/Leetcode13_RomanToInteger.py

"""

# romanToInt("IV")