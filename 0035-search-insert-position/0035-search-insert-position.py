class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1

        while l <=r:
            m = l + (r-l)//2
            num = nums[m] 

            if target == num:
                return m
            elif target > num:
                l = m+1
            else:
                r= m-1

        return l     