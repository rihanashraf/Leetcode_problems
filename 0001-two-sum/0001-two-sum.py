class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicti = {}
        for i in range(len(nums)):
            dicti[nums[i]] = i

        for i in range(len(nums)):
            num = target - nums[i]

            if num in dicti and dicti[num] !=i:
                return [i, dicti[num]]
        