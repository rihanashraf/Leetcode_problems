class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dicti = {}
        for num in nums:
            if num not in dicti:
                dicti[num] = 1
            else:
                return True
        return False

