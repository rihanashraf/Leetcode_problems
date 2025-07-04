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
                if not arr:
                    return False
                else:
                    popped = arr.pop()
                    if popped != dicti[char]:
                        return False
        return not arr
