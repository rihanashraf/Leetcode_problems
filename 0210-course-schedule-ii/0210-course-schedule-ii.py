class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        D = defaultdict(list)
        for a, b in prerequisites:
            D[a].append(b)

        unvisited = 0
        visiting = 1 
        visited =2
        states = [unvisited] * numCourses

        def dfs(node):
            if states[node] == visited:
                return True
            elif states[node] == visiting:
                return False

            states[node] = visiting

            for nei in D[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            order.append(node)
            return True

        order = []

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order