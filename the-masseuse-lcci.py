# 面试题 17.16. 按摩师
# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
# 注意：本题相对原题稍作改动


# 示例 1：

# 输入： [1,2,3,1]
# 输出： 4
# 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
# 示例 2：

# 输入： [2,7,9,3,1]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
# 示例 3：

# 输入： [2,1,4,5,3,1,1,3]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

# 来源：Leetcode
# 链接：https://leetcode-cn.com/problems/the-masseuse-lcci/


class Solution:
    def massage1(self, nums) -> int:
        """ 动态规划 """
        if not nums: return 0

        dp = [[0, 1] for _ in range(len(nums))]
        dp[0] = [0, nums[0]]

        for i in range(1, len(nums)):
            for j in (0, 1):
                can_reserve = dp[i - 1][0] + nums[i] if j == 1 else dp[i - 1][0]
                can_not_reverse = dp[i - 1][1]
                dp[i][j] = max(can_reserve, can_not_reverse)

        return max(dp[len(nums) - 1])

    def massage(self, nums) -> int:
        """ 动态规划 """
        if not nums: return 0

        dp0 = 0
        dp1 = nums[0]

        for i in range(1, len(nums)):
            can_reserve = dp0
            can_not_reverse = dp1
            dp0 = max(can_reserve, can_not_reverse)
            dp1 = max(can_reserve + nums[i], can_not_reverse)

        return max(dp0, dp1)


if __name__ == "__main__":
    assert Solution().massage([1,2,3,1]) == 4
    assert Solution().massage([2,7,9,3,1]) == 12
    assert Solution().massage([2,1,4,5,3,1,1,3]) == 12
    assert Solution().massage([1]) == 1
    assert Solution().massage([1, 2]) == 2
