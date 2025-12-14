class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti = {}
        for a in s:
            if a in dicti:
                dicti[a] +=1
            else:
                dicti[a] = 1
            
            
        for b in t:
            if b in dicti and dicti[b] != 0:
                dicti[b] -=1
            else:
                return False
        return True if len(s) == len(t) else False 