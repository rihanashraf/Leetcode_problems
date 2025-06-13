class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        hashmap = {")": "(", "}" : "{", "]": "["}
        stk = []

        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False
        return not stk