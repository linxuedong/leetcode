# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

# 示例 1:
# 输入: 2
# 输出: [0,1,1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/counting-bits
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def countBits1(self, num: int):
        rst = []
        for i in range(num + 1):
            count = 0
            n = i
            while n != 0:
                n &= n - 1
                count += 1
            rst.append(count) 
        return rst

    def countBits(self, num: int):
        count = list(range(num + 1))
        for i in count[1:]:
            count[i] = count[i&(i-1)] + 1
        return count 


if __name__ == "__main__":
    print(Solution().countBits(5))
    assert Solution().countBits(5) == [0,1,1,2,1,2]