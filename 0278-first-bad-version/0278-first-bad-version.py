# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l=1
        r = n

        while l<=r:
            m = l+(r-l)//2
            if l ==m and isBadVersion(m) == True:
                return l
            elif isBadVersion(m) == True:
                r = m
            else:
                l = m+1
            
        