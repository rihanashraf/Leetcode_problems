class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        for number in nums:
            output.append(number**2)
        output.sort()
        return output

        
        