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
        
        for i in range(len(new_s)):
            j = -i-1
            if new_s[i]!= new_s[j]:
                return False
        return True