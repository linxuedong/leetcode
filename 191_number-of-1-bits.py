# 191. 位1的个数
# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

# 示例 1：
# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-1-bits

class Solution:
    def hammingWeight1(self, n: int) -> int:
        """ 
        方法一
        1. 将数字取余数，判断是否为 2
        2. 数字整除 2
        """
        count = 0
        while n != 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count
        
    def hammingWeight2(self, n: int) -> int:
        """ 方法一的位运算 """
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count

    def hammingWeight(self, n:int) -> int:
        """ 方法三 
        n & (n - 1) 为去掉 n 的最后一个 1

        n  :     1(1)000 
        n-1:   & 1 0 111
               = 1 0 000

        去掉最后一个数值为 0，去掉几次则为结果
        """
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count
