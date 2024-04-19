class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        islandnum = 0
        def rec(r,c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return
            if r-1 >= 0:
                rec(r-1, c)
            if r+1 < m:
                rec(r+1, c)
            if c-1 >=0:
                rec(r, c-1)
            if c+1 < n:
                rec(r, c+1)
        
        for _r in range(0,m):
            for _c in range(0,n):
                if grid[_r][_c] == '1':
                    islandnum += 1
                    rec(_r, _c)
        return islandnum