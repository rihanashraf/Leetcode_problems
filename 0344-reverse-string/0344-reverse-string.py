class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)/2+len(s)%2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1],s[i]
        return s