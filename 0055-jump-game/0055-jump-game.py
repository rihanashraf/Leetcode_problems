class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i =0
        while i <len(nums):
            if nums[i] == 0 and i !=0:
                i -=1
            elif len(nums) == 1:
                return True
            elif nums[i] == 0 and i ==0:
                return False
            elif i +nums[i] >=len(nums)-1:
                return True
            elif nums[nums[i] +i] ==0:
                nums[i] -=1
            else:
                i+=nums[i]
        