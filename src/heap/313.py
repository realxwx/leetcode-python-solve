#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        跟丑数的题一样，不断去比较
        优先队列
        :param n:
        :param primes:
        :return:
        """
        import heapq
        a = [0 for _ in range(len(primes))]
        print("a=", a)
        # 求很多次最小值
        res = 1
        heap = []
        for i in range(1, n):
            for p in primes:
                t = p * res
                heapq.heappush(heap, t)
            res = heapq.heappop(heap)
            while heap and res == heap[0]:
                heapq.heappop(heap)
        return res
