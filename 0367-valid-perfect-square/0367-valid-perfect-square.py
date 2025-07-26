class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = 2**16

        while l <= r:
            m = l+(r-l)//2
            square = m*m 

            if num == square:
                return True
            elif square> num:
                r = m-1
            else:
                l = m+1
        return False    