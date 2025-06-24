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

        arr = nums1 + nums2
        arr.sort()
        i = 0
        while i != (len(arr)/2):
            j = -i-1
            if i == j:
                return arr[i]
            i+=1
        j = -i-1
        return ((float(arr[i])+float(arr[j]))/2)

