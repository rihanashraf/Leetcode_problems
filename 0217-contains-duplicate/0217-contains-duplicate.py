class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dicti = {}

        for number in nums:
            if number not in dicti:
                dicti[number] = 1
            else:
                return True
        return False
        