class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        i = 0
        j = 1 
        if nums == []:
            return []
        elif len(nums) ==1:
            nums[0] = str(nums[0])
            return nums
        start = nums[i]

        while j < len(nums):
            if nums[j] - nums[i] > 1:
                if start != nums[i]:
                    new_list = str(start) + "->" + str(nums[i])
                else:
                    new_list = str(start)
                ranges.append(new_list)
                start = nums[j]
            if j == len(nums)-1:
                if start != nums[j]:
                    new_list = str(start) + "->" + str(nums[j])
                else:
                    new_list = str(start)
                ranges.append(new_list)
            i +=1
            j +=1
        return ranges
        


            


        