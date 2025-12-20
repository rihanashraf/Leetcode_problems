class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        master = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14,"p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y": 24, "z":25}   
        dicti = {}
        ci = 0
        for s in strs:
            count = [0] * 26
            for c in s:
                count[master[c]] +=1
            if tuple(count) in dicti:
                res[dicti[tuple(count)]].append(s)
            else:
                dicti[tuple(count)] = ci
                res.append([s])
                ci+=1

        return res
            
            

                    

        