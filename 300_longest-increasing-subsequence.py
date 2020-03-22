# 300. 最长上升子序列

# 给定一个无序的整数数组，找到其中最长上升子序列的长度。

# 示例:
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS1(self, nums):
        """ 动态规划 """
        if not nums: return 0

        DP = [None for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                DP[i] = 1

            max_dp_j = [0]
            for j in range(i):
                
                if nums[j] < nums[i]:
                    max_dp_j.append(DP[j])
            
            DP[i] = max(max_dp_j) + 1
        return max(DP)

    def lengthOfLIS2(self, nums):
        """ 动态规划法 """
        if not nums: return 0

        # DP[i] 为选中 nums[i] 的最长上升子序列
        DP = [1 for _ in range(len(nums))]
        result = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[i], DP[j] + 1)
            result = max(result, DP[i])
        return result

    def lengthOfLIS(self, nums):
        """ 二分查找法 """
        if not nums: return 0

        result = []

        for num in nums:
            if not result or num > result[-1]:
                result.append(num)
            else:
                l, r = 0, len(result) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if result[mid] >= num:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                result[loc] = num

        return len(result)


if __name__ == "__main__":
    assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
    # assert Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6
        