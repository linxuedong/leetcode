# 547. 朋友圈
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

# 示例 1:
# 输入: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。

# 示例 2:
# 输入: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。

# 注意：
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/friend-circles
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class UnionFind:
    def __init__(self, M):
        m = len(M)

        self.parent = [i for i in range(m)]
        self.rank = [0] * m
        self.count = m
        
        
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
            self.count -= 1

class Solution1:
    """ 并查集 """
    def findCircleNum(self, M):
        if not M: return 0

        m = len(M)
        uf = UnionFind(M)

        for i in range(m):
            for j in range(m):
                if M[i][j] == 1 and i != j:
                    uf.union(i, j)

        return uf.count


class Solution:
    def dfs(self, M, i):
        for j in range(len(M)):
            if M[i][j] == 1 and j not in self.visited:
                self.visited.add(j)
                self.dfs(M, j)

    def findCircleNum(self, M):
        """ 深度优先法 """
        self.visited = set()
        count = 0
        for i in range(len(M)):
            if i not in self.visited:
                self.dfs(M, i)
                count += 1
        return count


if __name__ == "__main__":
    M = [[1,1,0],
        [1,1,0],
        [0,0,1]]
    assert Solution().findCircleNum(M) == 2

    M = [[1,1,0],
        [1,1,1],
        [0,1,1]]
    assert Solution().findCircleNum(M) == 1
