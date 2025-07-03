class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n-1

        while l<r:
            m = l+(r-l)//2
            mid = nums[m]
            if mid >nums[r]:
                l = m+1
            else:
                r=m 
        return nums[l]
        