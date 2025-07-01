class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l =1
        r = (2**15)*1.44
        
        while l <= r:
            m = l+(r-l)//2
            res = m*m

            if res == num:
                return True
            elif res < num:
                l = m+1
            else:
                r= m-1
        return False

        
