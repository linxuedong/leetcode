# 面试题 01.04. 回文排列
# 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
# 回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
# 回文串不一定是字典当中的单词。

# 示例1：
# 输入："tactcoa"
# 输出：true（排列有"tacocat"、"atcocta"，等等）

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import Counter

class Solution:
    def canPermutePalindrome1(self, s: str) -> bool:
        """ 哈希表 """
        count = Counter(s).values()
        result = 0

        for v in count:
            result += v // 2 * 2
            # result 是偶数， v 是奇数
            if result & 1 == 0 and v & 1 == 1:
                result += 1

        return result == len(s)

    def canPermutePalindrome(self, s: str) -> bool:
        """ 哈希表 二"""
        count = Counter(s).values()
        length = len(s)

        for v in count:
            length -= v // 2 * 2
        
        return length <= 1
    


if __name__ == "__main__":
    assert Solution().canPermutePalindrome("tactcoa") == True
    assert Solution().canPermutePalindrome('abc') == False
    assert Solution().canPermutePalindrome('aab') == True
        