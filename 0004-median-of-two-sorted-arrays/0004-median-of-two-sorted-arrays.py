class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #time : O(log(m+n))
        #use bsa

        arr = []

        i = 0
        j = 0

        while i != len(nums1) and j != len(nums2):
            if nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j +=1
            else:
                arr.append(nums1[i])
                i+=1
        if i != len(nums1):
            while i != len(nums1):
                arr.append(nums1[i]) 
                i+=1
        else:
            while j != len(nums2):
                arr.append(nums2[j]) 
                j +=1
        i = 0
        while i != (len(arr)/2):
            j = -i-1
            if i == j:
                return arr[i]
            i+=1
        j = -i-1
        return ((float(arr[i])+float(arr[j]))/2)

