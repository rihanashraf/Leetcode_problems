class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        n = len(nums)
        r = len(nums)-1

        while l <r:
            m = l+(r-l)//2
            mid = nums[m]
            if nums[r]< mid:
                l = m+1
            else:
                r = m
        minimum = l
        
        if minimum ==0:
            l, r = 0, n-1
        elif target >=nums[0] and target<= nums[minimum-1]:
            l, r = 0, minimum-1
        else:
            l,r = minimum, n-1
        
        while l<=r:
            m = l+(r-l)//2
            print(nums[m])
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r= m-1
        return -1




            
                    