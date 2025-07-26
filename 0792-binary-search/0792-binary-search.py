class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <=right:
            mid = left + (right-left)//2
            number = nums[mid]

            if target == number:
                return mid
            elif target > number:
                left = mid +1
            else:
                right = mid -1
            
        return -1
        