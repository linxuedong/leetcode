class Solution:
    def maxProfit1(self, prices):
        """ 贪心算法: 方法1 """
        pre = None
        result = 0

        for cur in prices:
            if pre is None:
                pre = cur
                continue

            if cur > pre:
                result += cur - pre
            pre = cur
        return result

    def maxProfit(self, prices):
        """ 贪心算法: 方法2 """
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res


if __name__ == "__main__":
    assert Solution().maxProfit([7,1,5,3,6,4]) == 7
    assert Solution().maxProfit([7,6,4,3,1]) == 0
                
            


