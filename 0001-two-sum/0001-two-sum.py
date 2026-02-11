class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}        
        for i in range(len(nums)):
            dicti[nums[i]] = i
        for i in range(len(nums)):
            number = target - nums[i]
            if number in dicti and dicti[number] != i:
                return [i, dicti[number]]
