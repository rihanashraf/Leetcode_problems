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
            letter = s[i]
            andi = t[j]
            if letter == andi:
                i +=1
                j+=1
            else:
                j +=1
        
        return True if i == len(s) else False


        