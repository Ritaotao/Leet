#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        r = int(str(sign * x)[::-1])
        return sign * r * (r < 2**31)

