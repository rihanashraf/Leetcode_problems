class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s)-1
        k=1
        while i >=0:
            if s[len(s)-k] == " ":
                k+=1
            elif s[i] != " ":
                length +=1
            else:
                return length
            i-=1
        return length