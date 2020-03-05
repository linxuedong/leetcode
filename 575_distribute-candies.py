from collections import defaultdict

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        get_candies_num = int(len(candies) / 2)
        candies_type = defaultdict(int)
        for type in candies:
            candies_type[type] += 1

        candies_type_num = len(candies_type)

        if get_candies_num > candies_type_num:
            return candies_type_num
        else:
            return get_candies_num

    def distributeCandies1(self, candies]) -> int:
        candies_type = set(candies)
        get_candies_num = len(candies) // 2
        return min(len(candies_type), get_candies_num)