class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        sep_digist = self.seprateDigist(N)
        not_increas_index = self.checkNotIncreasingIndex(sep_digist)

        while not_increas_index is not None:
            i = not_increas_index
            for j in range(i + 1, len(sep_digist)):
                sep_digist[j] = 9
            sep_digist[i] -= 1
            not_increas_index = self.checkNotIncreasingIndex(sep_digist)

        return self.mergeDigist(sep_digist)

    def mergeDigist(self, lst):
        result = 0
        count = 0
        lst.reverse()

        for i in lst:
            result = result + i * 10 ** count
            count += 1

        return result

    def seprateDigist(self, N):
        """
        将数值按位分割为列表
        """
        result = []
        while N:
            mod = N % 10
            N = N // 10
            result.insert(0, mod)
        return result

    def checkNotIncreasingIndex(self, lst):
        """
        检查数值有没有单调递增
        """
        x = lst[0]
        for i, y in enumerate(lst[1:]):
            if x <= y:
                x = y
            else:
                return i


if __name__ == "__main__":
    assert Solution().seprateDigist(332) == [3, 3, 2]
    assert Solution().seprateDigist(1234) == [1,2,3,4]
    assert Solution().seprateDigist(1230) == [1,2,3,0]
    
    assert Solution().checkNotIncreasingIndex([1,2,3,4]) is None
    assert Solution().checkNotIncreasingIndex([3,3,2]) == 1
    
    assert Solution().mergeDigist([1,2,3,4]) == 1234
    assert Solution().mergeDigist([1, 2, 3, 0]) == 1230
    assert Solution().monotoneIncreasingDigits(332) == 299
    assert Solution().monotoneIncreasingDigits(100) == 99
