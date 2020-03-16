# 120. 三角形最小路径和
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def minimumTotal1(self, triangle) -> int:
        """ 
        递归法
        时间复杂度 O(2 ^ n) 
        """
        def _helper(i, j):
            # 递归终止条件

            if i == len_triangle - 1:
                return triangle[i][j]
            
            left = _helper(i + 1, j) + triangle[i][j]
            right = _helper(i + 1, j + 1)  + triangle[i][j]
            return min(left, right)

        len_triangle = len(triangle)
        return _helper(0, 0)

    def minimumTotal2(self, triangle):
        """
        动态规划
        时间复杂度 O(n^2)
        """
        dp = [[None for _ in row] for row in triangle]

        for i in range(len(triangle) - 1, -1, -1):
            for j in range(len(triangle[i])):
                if i == len(triangle) - 1:
                    dp[i][j] = triangle[i][j]
                else:
                    left = triangle[i][j] + dp[i + 1][j]
                    right = triangle[i][j] + dp[i + 1][j + 1]
                    dp[i][j] = min(left, right)
        return dp[0][0]

    def minimumTotal(self, triangle) -> int:
        """ 动态规划优化 """
        buttom = triangle[-1]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                buttom[j] = min(buttom[j], buttom[j + 1]) + triangle[i][j]
        return buttom[0]



if __name__ == "__main__":
    triangle = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    print(Solution().minimumTotal(triangle))