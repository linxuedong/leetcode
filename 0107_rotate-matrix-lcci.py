# 面试题 01.07. 旋转矩阵
# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
# 不占用额外内存空间能否做到？

# 来源：Leetcode
# 链接：https://leetcode-cn.com/problems/rotate-matrix-lcci/

class Solution:
    def rotate1(self, matrix) -> None:
        """
        占用额外内存空间
        """
        if matrix == []: return []

        N = len(matrix)
        result = [[] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                result[i].append(matrix[N-j-1][i])

    def rotate2(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        copy_matrix = [[num for num in matrix[i]] for i in range(N) ]
        
        for i in range(N):
            for j in range(N):
                matrix[i][j] = copy_matrix[N-j-1][i]

    def rotate3(self, matrix) -> None:
        N = len(matrix)
        r = list(zip(*matrix[::-1]))
        for i in range(N):
            for j in range(N):
                matrix[i][j] = r[i][j]
        return matrix

    def rotate(self, matrix) -> None:
        """ 空间复杂度为 O(1), 时间复杂度O(N^2) """
        # [[1,2,3],
        # [4,5,6],
        # [7,8,9]]
        
        N = len(matrix)
        # 水平翻转
        # [[7,8,9],
        # [4,5,6],
        # [1,2,3]]

        for i in range(N // 2):
            for j in range(N):
                matrix[i][j], matrix[N-i-1][j] = matrix[N-i-1][j], matrix[i][j]

        # 主对角线翻转
        # [[7,4,1],
        # [8,5,2],
        # [9,6,3]]
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    result = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    assert Solution().rotate(matrix) == result
    matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    result = [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]
    assert Solution().rotate(matrix) == result
 

