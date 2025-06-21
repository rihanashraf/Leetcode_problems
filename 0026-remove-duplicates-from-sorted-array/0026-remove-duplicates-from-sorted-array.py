class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #concept of k pointer in place?

        k = 0

        for i in range(len(nums)):
            if nums[i] != nums[k]:
                nums[k+1] = nums[i]
                k+=1
        return k+1 