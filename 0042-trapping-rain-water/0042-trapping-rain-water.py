class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # GREG's solution
        l = r = 0
        n = len(height)
        max_left = [0]*n # arrays for storing max_left and max_right at every index
        max_right = [0]*n   

        for i in range(n):
            j = -i -1 #when i moves forward, j moves with it backward, from the back
            max_left[i] = l
            max_right[j] = r
            l = max(l, height[i])
            r = max(r, height[j])
        
        res = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            res += max(0, pot - height[i])
        return res

        #kinda hard, go through again later for greater clarity of concepts
        #Time: O(n), cause looping through the height loop multiple times
        #Space : O(n), cause making new arrays of same length as that of height

        