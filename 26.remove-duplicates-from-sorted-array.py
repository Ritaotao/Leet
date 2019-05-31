#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        while cur < len(nums) - 1:
            if nums[cur] == nums[cur+1]:
                del nums[cur]
                cur -= 1
            cur += 1
        return len(nums)

