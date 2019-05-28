#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        output = 0
        buffer = 0
        for char in s:
            if buffer > 0:
                if map[char] > buffer:
                    output += map[char] - buffer
                    buffer = 0
                else:
                    output += buffer
                    buffer = map[char]
            else:
                buffer = map[char]
        return output + buffer
        

