# 231. 2的幂
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 示例 1:
# 输入: 1
# 输出: true
# 解释: 20 = 1

# 链接：https://leetcode-cn.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo1(self, n: int) -> bool:
        """ 方法一 """
        cur = 1
        for i in range(31):
            if n == cur:
                return True
            cur *= 2
        return False

    def isPowerOfTwo(self, n: int) -> bool:
        """ 方法二 
        n & (n - 1) 删除 n 的最后一位 1
        2 的幂次方二进制数字，只有一个 1
        如： 2: 10      4: 100      8: 1000
        """
        if n == 0: return False
        n &= n - 1
        return n == 0