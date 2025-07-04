class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dicti = {"]":"[", "}":"{", ")" : "("}
        arr = []

        for char in s:
            if char not in dicti:
                arr.append(char)
            else:
                if dicti[char] in arr and dicti[char]==arr[-1]:
                    print("yes")
                    arr.pop()
                else:
                    return False
        return not arr
