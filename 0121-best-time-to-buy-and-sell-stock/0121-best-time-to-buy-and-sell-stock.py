class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_number = float('inf')

        for price in prices:
            if price < min_number:
                min_number = price

            profit = price - min_number

            if profit > max_profit:
                max_profit = profit

        return max_profit


        

        


            

        