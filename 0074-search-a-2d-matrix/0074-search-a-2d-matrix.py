class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m -1

        while l <= r:
            mid= l +(r-l)//2
            s = matrix[mid][0] 
            if target == s:
                return True
            elif target < s:
                r = mid-1
            else:
                l = mid+1
        mid = l +(r-l)//2

        l = 0
        r = n-1

        while l <=r:
            midd= l +(r-l)//2
            s = matrix[mid][midd] 
            if target == s:
                return True
            elif target < s:
                r = midd-1
            else:
                l = midd+1
        return False
    

                
        