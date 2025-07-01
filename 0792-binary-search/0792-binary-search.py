class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #basic algorithm

        l = 0
        r = len(nums)-1

        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return -1

        
                
        