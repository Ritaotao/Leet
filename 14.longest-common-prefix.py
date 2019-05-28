#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        cl = min([len(x) for x in strs])
        output = ""
        if cl == 0:
            return output
        for i in range(cl):
            current = strs[0][i]
            for st in strs[1:]:
                if st[i] != current:
                    return output
            output += current            
        return output

        

