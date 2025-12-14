class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicti = {}
        for element in nums:
            if element in dicti:
                return True
            else:
                dicti[element] = element

        return False
