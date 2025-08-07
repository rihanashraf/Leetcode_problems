class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        #convert to adjacency list
        if source == destination:
            return True

        D = defaultdict(list)

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)

        seen = set()
        seen.add(source)

        ans = [False]
        def dfs(node):
            for node in D[node]:
                if node == destination:
                    ans[0] = True
                if node not in seen:
                    seen.add(node)
                    dfs(node)

        dfs(source)
        return ans[0]
                
        