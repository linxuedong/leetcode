# 面试题 01.02. 判定是否互为字符重排
# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

# 示例 1：
# 输入: s1 = "abc", s2 = "bca"
# 输出: true 

# 示例 2：
# 输入: s1 = "abc", s2 = "bad"
# 输出: false

# 说明：
# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100

# 链接：https://leetcode-cn.com/problems/check-permutation-lcci/

from collections import Counter

class Solution:
    
    def CheckPermutation1(self, s1: str, s2: str) -> bool:
        """ 排序 """
        if len(s1) != len(s2): return False

        a = list(s1)
        b = list(s2)
        a.sort()
        b.sort()
        return a == b

    def CheckPermutation2(self, s1: str, s2: str) -> bool:
        """ 哈希表 """ 
        if len(s1) != len(s2): return False

        count1 = Counter(s1)
        count2 = Counter(s2)
        return count1 == count2

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        a = {}
        b = {}
        for i in s1:
            a[i] = a.get(i, 0) + 1
        
        for i in s2:
            b[i] = b.get(i, 0) + 1
        return a == b


if __name__ == "__main__":
    assert Solution().CheckPermutation('abc', 'cba') == True
    assert Solution().CheckPermutation('abb', 'aab') == False
