class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #O(n) time- top down memoization
        #O(n) space - recursive call stack is the height of the tree
        dicti = {0:0, 1:1}
        def fib(n):
            if n in dicti:
                return dicti[n]
            
            else:
                dicti[n] = fib(n-1) + fib(n-2)
                return dicti[n]

        return fib(n)

            





        