class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []

        for i in range(len(operations)):
            if operations[i] == "+":
                record.append(record[-1]+record[-2])
            elif operations[i] == "D":
                record.append(2*record[-1])
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)
        