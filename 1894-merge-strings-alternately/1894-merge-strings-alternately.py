class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ''
        i=0
        while i < min(len(word1), len(word2)):
            merged +=word1[i]
            merged +=word2[i]
            i+=1

        while i < len(word1):
            merged+=word1[i]
            i+=1
        
        while i < len(word2):
            merged +=word2[i]
            i+=1
        return merged