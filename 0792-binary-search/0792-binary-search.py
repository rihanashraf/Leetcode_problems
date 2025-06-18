class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range((len(nums)/2)+len(nums)%2):
            j = -i-1
            if nums[i] == target:
                return i
            elif nums[j] == target:
                return len(nums) + j 
        return -1
        