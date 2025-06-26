class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        for i in range(0, 100000):
            if i*i <= x:
                ans = i
            elif i*i >x:
                break
        return ans