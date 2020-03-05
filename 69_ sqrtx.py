class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x // 2
        while left <= right:
            mid = (right + left) / 2
            if int(mid * mid) == x:
                return int(mid)
            elif mid * mid > x:
                right = mid
            else:
                left = mid

if __name__ == "__main__":
    res = Solution().mySqrt(8)
    print(res)
    import math
