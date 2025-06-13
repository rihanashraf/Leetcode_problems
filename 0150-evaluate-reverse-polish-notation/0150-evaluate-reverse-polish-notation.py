class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        s = 0
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token == "+":
                s = stk[-2] + stk[-1]
                stk.pop()
                stk.pop()
                stk.append(s)
            elif token == "-":
                s = stk[-2] - stk[-1]
                stk.pop()
                stk.pop()
                stk.append(s)
            elif token == "*":
                s = stk[-2] * stk[-1]
                stk.pop()
                stk.pop()
                stk.append(s)
            elif token == "/":
                s = int(stk[-2] / stk[-1])
                stk.pop()
                stk.pop()
                stk.append(s)
            else:
                stk.append(float(token)) 
        return int(s)