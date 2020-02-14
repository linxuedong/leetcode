class Solution:

    def myPow1(self, x: float, n: int) -> float:
        """
        暴力法
        >>> Solution().myPow1(2, 10)
        1024
        >>> Solution().myPow1(3, 3)
        27
        >>> Solution().myPow1(2, -2)
        0.25
        """
        result = 1

        if n == 0:
            return result
        while n > 0:
            n -= 1
            result *= x
        
        while n < 0:
            n += 1
            result *= (1 / x)
        return result

    def myPow(self, x: float, n: int) -> float:
        """ 分治法 
        >>> Solution().myPow(2, 10)
        1024
        >>> Solution().myPow(3, 3)
        27
        >>> Solution().myPow(2, -2)
        0.25
        """
        if n == 0: return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        # 为奇数
        if n % 2:
            return self.myPow(x, n - 1) * x
        # 为偶数
        return self.myPow(x * x, n / 2)

        




if __name__ == "__main__":
    import doctest
    doctest.testmod()