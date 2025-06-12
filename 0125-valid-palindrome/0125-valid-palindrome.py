class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= s.lower()
        s = ''.join(char for char in s if char.isalnum())
        print(s)

        for i in range(len(s)/2+len(s)%2):
            if s[i] == s[len(s)-i-1]:
                continue
            else:
                return False
        return True       
