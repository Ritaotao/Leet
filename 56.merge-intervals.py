#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if output and i[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output.append(i)
        return output
        

