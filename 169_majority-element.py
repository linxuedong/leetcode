from collections import Counter

class Solution:
    def majorityElement1(self, nums):
        """
        哈希表法
        >>> Solution().majorityElement1([3,2,3])
        3
        >>> Solution().majorityElement1([2,2,1,1,1,2,2])
        2
        """
        count = Counter(nums)
        return max(count, key=count.get)

    def majorityElement(self, nums):
        """
        哈希表法
        >>> Solution().majorityElement([3,2,3])
        3
        >>> Solution().majorityElement([2,2,1,1,1,2,2])
        2
        """
        dct = {}
        for i in nums:
            dct[i] = dct.get(i, 0) + 1
        
        return max(dct.keys(), key= dct.get)

    def majorityElement2(self, nums):
        """
        暴力法

        >>> Solution().majorityElement([3,2,3])
        3
        >>> Solution().majorityElement([2,2,1,1,1,2,2])
        2
        """
        majority_count = len(nums) / 2
        for num in nums:
            count = sum(1 for i in nums if i == nun)
            if count > majority_count:
                return num

    def majorityElement3(self, nums):
        """
        排序

        >>> Solution().majorityElement([3,2,3])
        3
        >>> Solution().majorityElement([2,2,1,1,1,2,2])
        2
        """
        nums.sort()
        # 多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素
        # 所以排序后在索引为 n / 2 对应的值是正确的
        return nums[len(nums) // 2]

    def majorityElement4(self, nums):
        """
        分治
        """
        def majority_element_rec(lo, hi):
            # 左右下标一致
            if lo == hi:
                return nums[lo]
            
            mid = (hi - lo) // 2 + lo    
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            if left == right:
                return left
            
            left_count = sum(1 for i in range(lo, hi+1,) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)
            return left if left_count > right_count else right

            

        return majority_element_rec(0, len(nums)-1)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    Solution().majorityElement4([2,2,1,1,1,2,2])