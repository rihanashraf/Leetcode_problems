class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dicti = {}
        for element in nums:
            if element not in dicti:
                dicti[element] = 1
            elif element in dicti:
                return True
        return False