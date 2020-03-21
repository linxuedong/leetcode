# 121. 买卖股票的最佳时机

# 给定一个数组，它的第 i 元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。

# 示例 1:

# 输入: [7, 1, 5, 3, 6, 4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6 - 1 = 5 。
# 注意利润不能是 7 - 1 = 6, 因为卖出价格需要大于买入价格。

# 示例 2:

# 输入: [7, 6, 4, 3, 1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit1(self, prices):
        """ 暴力法 """

        if not prices: return 0
        price = 0

        for i in range(1, len(prices)):
            buy = min(prices[:i])
            sale = max(prices[i:])
            price = max(price, sale - buy)

        return price

    def maxProfit2(self, prices):
        if not prices: return 0
        price = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                price = max(price, prices[j] - prices[i])

        return price

    def maxProfit3(self, prices):
        if len(prices) < 2: return 0

        buy, sale = prices[0], prices[1]
        price = max(sale - buy, 0)

        for i in range(1, len(prices) - 1):
            price1 = prices[i]
            price2 = prices[i + 1]
            if buy > price1:
                buy = price1
                sale = price2
            if sale < price2:
                sale = price2

            price = max(sale - buy, price)
        return price

    def maxProfit(self, prices):
        result = 0
        buy = int(1e9)

        for price in prices:
            result = max(price - buy, result)
            buy = min(buy, price)

        return result


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    assert Solution().maxProfit([1,2]) == 1



