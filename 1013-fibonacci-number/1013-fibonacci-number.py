class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #O(n) - top down memoization
        dicti = {0:0, 1:1}
        def fib(n):
            if n in dicti:
                return dicti[n]
            
            else:
                dicti[n] = fib(n-1) + fib(n-2)
                return dicti[n]

        return fib(n)

            





        