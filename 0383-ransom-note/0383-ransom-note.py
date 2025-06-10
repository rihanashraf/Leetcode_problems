class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dicti = {}
        for letter in magazine:
            if letter not in dicti:
                dicti[letter] = 1
            else:
                dicti[letter] +=1
        
        for letter in ransomNote:
            if letter in dicti and dicti[letter] !=0:
                dicti[letter] -= 1
            else:
                return False
        return True
        


        
            
            
        