class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = ""

        for char in s:
            if char.isalnum():
                new_s += char
        
        for i in range(len(new_s)/2):
            if new_s[i]!= new_s[len(new_s)-i-1]:
                return False
        return True