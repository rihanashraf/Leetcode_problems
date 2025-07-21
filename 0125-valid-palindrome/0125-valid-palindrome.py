class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        
        for i in range(len(s)):
            j = -i-1
            if s[i] != s[j]:
                return False
        return True
        