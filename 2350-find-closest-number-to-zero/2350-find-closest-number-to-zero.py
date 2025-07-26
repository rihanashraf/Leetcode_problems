class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for number in nums:
            if number == abs(ans):
                ans = number
            elif abs(number) < abs(ans):
                ans = number
        return ans
        