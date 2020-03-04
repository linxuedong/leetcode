class Solution:
    def orangesRotting(self, grid) -> int:
        self.I = len(grid)
        self.J = len(grid[0])

        if not grid: return None

        queue = []

        d = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append((i, j, d))

        while queue:
            cur_i, cur_j, d = queue.pop(0)

            # 查看相邻橘子是否腐烂
            for n_i, n_j in self.nieghbors(cur_i, cur_j):
                if grid[n_i][n_j] == 1:
                    grid[n_i][n_j] =  2
                    queue.append((n_i, n_j, d + 1))

        if any(1 in row for row in grid):
            return -1

        return d
    
    def nieghbors(self, i, j):
        """ 查找当前位置 4 个正方向上的邻居 """
        for ni, nj in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
            if 0 <= ni < self.I and 0 <= nj < self.J:
                yield ni, nj


if __name__ == "__main__":
    a = [[2,1,1],[1,1,0],[0,1,1]]
    res = Solution().orangesRotting(a)
    print(res)
            
