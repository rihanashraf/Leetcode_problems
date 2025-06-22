class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = 0
        length = 0
        temp = x
        if x <0:
            return False

        while temp!=0:
            length +=1
            temp= temp/10
        
        temp = x
        while temp!=0:
            num = temp%10
            number += num*10**(length-1)
            length -=1
            temp = temp/10
        
        if number == x:
            return True
        return False
        