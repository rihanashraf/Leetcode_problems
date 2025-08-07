class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >=m or j >=n or grid[i][j] == "0":
                return 
            else:
                grid[i][j] = "0"
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)
                
        num_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands +=1
                    dfs(i, j)
        
        return num_islands




        