# 面试题 01.08. 零矩阵
# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
# 示例 1：
# 输入：
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出：
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2：
# 输入：
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出：
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zero-matrix-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def setZeroes1(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == []: return []
        m = len(matrix)
        n = len(matrix[0])

        x, y = self.find_zero(matrix)

        for i in x:
            matrix[i] = [0 for _ in range(n)]
        
        for j in y:
            for i in range(m):
                matrix[i][j] = 0

    def setZeroes(self, matrix) -> None:
        if max == []: return []
        m = len(matrix)
        n = len(matrix[0])

        x, y = self.find_zero(matrix)

        for i in range(m):
            for j in range(n):
                if i in x or j in y:
                    matrix[i][j] = 0

    @staticmethod
    def find_zero(matrix):
        x = set()
        y = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)

        return x, y

if __name__ == "__main__":
    input = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    output = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]

    assert Solution().setZeroes(input) == output

    input = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    output = [
        [0,0,0,0],
        [0,4,5,0],
        [0,3,1,0]
    ]
    assert Solution().setZeroes(input) == output
        
