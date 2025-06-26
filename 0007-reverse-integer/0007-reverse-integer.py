class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if x < 0:
                x = x*-1
                leng = 0
                temp =x
                while temp !=0:
                    leng +=1
                    temp = temp/10
                temp = x
                ans = 0
                while temp!=0:
                    num = temp %10
                    ans += num*10**(leng-1)
                    leng -=1
                    temp = temp /10
                ans = ans*-1
        else:
                leng = 0
                temp =x
                while temp !=0:
                    leng +=1
                    temp = temp/10
                temp = x
                ans = 0
                while temp!=0:
                    num = temp %10
                    ans += num*10**(leng-1)
                    leng -=1
                    temp = temp /10
        if ans > 2**31-1 or ans < -2**31:
            return 0
        return ans


            
        