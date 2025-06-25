class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        leng = 0
        temp = x
        if x<0:
            return False
        while temp!=0:
            leng+=1
            temp = temp/10
        
        pal = 0
        i = 1
        temp = x
        while temp!=0:
            num = temp%10
            pal += num*10**(leng-i)
            i+=1
            temp = temp /10
        
        return True if x == pal else False


        
        