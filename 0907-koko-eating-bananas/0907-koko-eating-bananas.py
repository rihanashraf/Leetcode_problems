class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # we have to search for k in [1, max[p]]
        l = 1
        r = max(piles)

        minimum = 0
        ans = -1
        while l <=r:
            k = l+(r-l)//2
            temp = h
            count =0
            for pile in piles:
                if pile < k:
                    count +=1
                elif pile%k == 0:
                    count += pile/k
                else:
                    count += (pile/k) +1
            print(count)
            if count <= h:
                r = k-1
                ans = k
            else:
                l = k+1
        return ans



            
