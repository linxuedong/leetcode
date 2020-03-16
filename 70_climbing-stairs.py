# 70. 爬楼梯

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。

# 示例 1：
# 输入： 2
# 输出： 2

# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/climbing-stairs/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def climbStairs1(self, n: int) -> int:
        """
        动态规划
        """
        self.memory = {1: 1, 2: 2}

        for i in  range(3, n + 1):
            self.memory[i] = self.memory[i -  1] + self.memory[i - 2]
   
        return self.memory[n]

    def climbStairs(self, n: int) -> int:
        """
        动态规划优化
        """
        one_step = 1
        two_step = 2
        for _ in range(3, n + 1):
            all_way = one_step + two_step
            one_step, two_step = two_step, all_way

        return all_way

    def climbStairs2(self, n: int) -> int:
        """ 
        递归法
        时间复杂度 O(2 ^ n) 
        """
        if 0 < n < 3:
            return n
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        
if __name__ == "__main__":
    print(Solution().climbStairs(38))