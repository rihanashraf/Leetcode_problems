class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l = m+n
        x = 0
        for i in range(m, l):
            nums1[i] = nums2[x]
            x+=1
        nums1.sort()
        