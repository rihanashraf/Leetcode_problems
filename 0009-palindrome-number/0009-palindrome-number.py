class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)

        for i in range(len(x)/2):
            j =-i-1
            if x[i] != x[j]:
                return False
        return True

        