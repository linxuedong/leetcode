# 200. 岛屿数量
# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

# 示例 1:
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1

# 示例 2:
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3

# 来源：Leetcode
# 链接：https://leetcode-cn.com/problems/number-of-islands/

class Solution1:
    """ 深度优先 """
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def numIslands(self, grid) -> int:
        if not grid: return 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.visited = set()
        return sum([self.floodfill_DFS(i, j) for j in range(self.n) for i in range(self.m)])

    def floodfill_DFS(self, i, j):
        if not self._is_land(i, j):
            return 0
        self.visited.add((i, j))
        for d in range(4):
            self.floodfill_DFS(i + self.dx[d], j + self.dy[d])
        return 1


    def _is_land(self, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False
        if self.grid[i][j] == '0' or (i, j) in self.visited:
            return False
        return True


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * ( m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

            self.count -= 1


class Solution:
    """ 并查集 """
    def numIslands(self, grid):
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        uf = UnionFind(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                
                for k in range(4):
                    nr, nc = i + dx[k], j + dy[k]
                    if nr >= 0 and nc >= 0 and nr <  m and nc < n and grid[nr][nc] == '1':
                        uf.union(i * n + j, nr * n + nc)

        return uf.count


if __name__ == "__main__":
    a= ["11110", "11010", "11000", "00000"]
    assert Solution().numIslands(a) == 1
    
    b = ["11000", "11000", "00100", "00011"]
    assert Solution().numIslands(b) == 3
