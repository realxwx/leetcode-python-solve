#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        a = []
        for l in matrix:
            for n in l:
                heapq.heappush(a, n)
        while a and k > 1:
            k -= 1
            heapq.heappop(a)
        return a[0]
