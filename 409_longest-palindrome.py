# 409. 最长回文串
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

# 注意:
# 假设字符串的长度不会超过 1010。

# 示例 1:
# 输入: "abccccdd"
# 输出: 7
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

from collections import Counter

class Solution:
    def longestPalindrome1(self, s: str) -> int:
        """ 贪心算法 """
        char_count = Counter(s)
        result = 0
        single_char = False

        for k, v in char_count.items():
            if v % 2 == 0:
                result += v
            elif v // 2 > 0:
                result += v // 2 * 2
                single_char = True
            else:
                single_char = True

        return result if not single_char else result + 1

    def longestPalindrome2(self, s: str) -> int:
        """ 方法一优化 """
        char_count = Counter(s)
        ans = 0

        for _, v in char_count.items():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

    def longestPalindrome(self, s: str) -> int:
        count = Counter(s).values()
        result = sum(v//2*2 for v in count if v // 2 > 0)
        return result if len(s) == result else result + 1

        
if __name__ == "__main__":
    s = 'abccccdd'
    assert Solution().longestPalindrome(s) == 7
    print(Solution().longestPalindrome('ccc'))
    assert Solution().longestPalindrome('ccc') == 3
