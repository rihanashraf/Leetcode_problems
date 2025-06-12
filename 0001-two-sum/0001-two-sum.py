class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #using hashmap
        dicti = {}
        for i in range(len(nums)):
            dicti[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in dicti and dicti[y] !=i:
                return [i, dicti[y]]
        

