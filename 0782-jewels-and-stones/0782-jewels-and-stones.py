class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        dicti = {}
        for jewel in jewels:
            dicti[jewel]  = 1
        ans = 0
        for stone in stones:
            if stone in dicti:
                ans+=1
        return ans
