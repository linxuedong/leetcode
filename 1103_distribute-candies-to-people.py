class Solution:
    def distributeCandies1(self, candies: int, num_people: int):
        distributed_candies = 0
        result = [0 for _ in range(num_people)]

        for c in range(1, candies):
            # 索引
            i = c % num_people - 1

            if distributed_candies + c > candies:
                # 将剩余的糖果发给最后一个小朋友
                result[i] += candies - distributed_candies
                distributed_candies += candies - distributed_candies
                return result
            else:
                result[i] += c
                distributed_candies += c

    def distributeCandies(self, candies, num_people):
        """
        >>> Solution().distributeCandies(candies = 7, num_people = 4)
        [1, 2, 3, 1]
        >>> Solution().distributeCandies(candies = 10, num_people = 3)
        [5, 2, 3]

        :param candies: 剩余需要发的糖果
        :param num_people: 小朋友数
        :return:
        """
        result = [0] * num_people
        i = 0

        while candies > 0:
            result[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()