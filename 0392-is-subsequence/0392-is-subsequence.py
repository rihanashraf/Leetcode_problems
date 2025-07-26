class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(s) and j < len(t):
                if t[j] == s[i]:
                    i+=1
                    j+=1
                else:
                    j+=1

        if i == len(s):
            return True
        else:
            return False