# 123. 买卖股票的最佳时机 III

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

# 示例 2:
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices) -> int:
        if not prices: return 0
        MAX_TRADE_TIMES = 2

        MP = [[[0, 0] for _ in range(MAX_TRADE_TIMES + 1)] for i in range(len(prices))]

        for i in range(len(prices)):

            # k 表示第 k 次交易
            for k in range(MAX_TRADE_TIMES):
                price = prices[i]

                if i == 0:
                    MP[i][k][0] = 0
                    MP[i][k][1] = - price
                    continue
                # 最后一位索引含义：
                # 0 为不拥有股票，后续可以买入
                # 1 为拥有股票，后续可以卖出

                # 第 i 次最优的结果为：第 i - 1 次不动，或者卖出股票
                do_nothing0 = MP[i - 1][k][0]
                sale = MP[i - 1][k][1] + price
                MP[i][k][0] = max(do_nothing0, sale)

                # 第 i 次最优的结果为：第 i - 1 次不动，或者买入股票
                do_nothing1 = MP[i - 1][k][1]
                buy = MP[i - 1][k - 1][0] - price
                MP[i][k][1] = max(do_nothing1, buy)

        result = 0
        for row in MP[-1]:
            result = max(row[0], result)
        return result

                     
if __name__ == "__main__":
    assert Solution().maxProfit([3,3,5,0,0,3,1,4]) == 6
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    assert Solution().maxProfit([1, 2]) == 1