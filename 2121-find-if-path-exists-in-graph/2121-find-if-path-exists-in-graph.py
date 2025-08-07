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
        def dfs(node):
            if node == destination:
                return True
            for node in D[node]:
                if node not in seen:
                    seen.add(node)
                    if dfs(node):
                        return True 
            return False
        return dfs(source)
                
        