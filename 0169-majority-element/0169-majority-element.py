class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicti = {}

        for element in nums:
            if element not in dicti:
                dicti[element] = 1
            else:
                dicti[element] +=1
        print(dicti)
        
        majority = nums[0]
        for element in nums:
            if dicti[element] >dicti[majority]:
                majority = element
            print(majority)
        return majority

