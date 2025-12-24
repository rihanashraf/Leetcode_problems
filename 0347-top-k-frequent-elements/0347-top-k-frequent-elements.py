class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        n = len(nums)

        for number in nums:
            if number in dicti:
                dicti[number] +=1
            else:
                dicti[number] = 1
        freq = []

        for i in range(n+1):
            freq.append([])
        

        for number in dicti:
            freq[dicti[number]].append(number)
        res = []

        for l in range(n, 0, -1):
            for number in freq[l]:
                res.append(number)
                if len(res) == k:
                    return res


                 
