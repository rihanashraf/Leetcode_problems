class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 0:
            return 0

        return self.fib(n-1) + self.fib(n-2)

        #naive recursive and hence is O(2^n), because at the last level it would be doubling, tree kinda approach
        #rememvber stuff in a dictionary for memoization, memo/cache for remembering
         
        