#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        open, close = '([{', ')]}'
        stack = []
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if not (stack and open.index(stack.pop()) == close.index(c)):
                    return False
        return not stack                    


