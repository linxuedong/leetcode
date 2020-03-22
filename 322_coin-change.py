# 322. 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change/

class Solution:

    def coinChange1(self, coins, amount):
        """ 动态规划法 """
        dp = [int(1e9) for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[-1] if dp[-1] != int(1e9) else -1

    def coinChange(self, coins, amount):
        """ 动态规划法 """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange(self, coins, amount):




if __name__ == '__main__':
    coins = [186, 419, 83, 408]
    amount = 6249

    coins = [2147483647]
    amount = 2
    print(Solution().coinChange(coins, amount))
    # assert Solution().coinChange([2], 3) == -1




