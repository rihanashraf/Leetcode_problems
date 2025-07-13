class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicti = {}
        for letter in s:
            if letter not in dicti:
                dicti[letter] = 1
            else:
                dicti[letter] +=1
        if len(s) != len(t):
            return False

        for letter in t:
            if letter in dicti and dicti[letter] > 0:
                dicti[letter] -=1
            else:
                return False
        return True
         
        