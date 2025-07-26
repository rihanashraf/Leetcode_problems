class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        ans = ''
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                ans+=strs[0][i]
            else:
                return ans
        return ans
        