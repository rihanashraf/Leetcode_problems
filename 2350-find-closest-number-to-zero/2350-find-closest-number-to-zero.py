class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = nums[0]
        for num in nums:
            if abs(num) < abs(final):
                final = num 
            elif num == abs(final):
                final = num
        return final


            


        