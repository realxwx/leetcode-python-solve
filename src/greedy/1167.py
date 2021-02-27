#  Copyright (c) 2021
#  @Author: xiaoweixiang
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        heap = []
        for n in sticks:
            heapq.heappush(heap, n)
        while len(heap) >= 2:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            c = a + b
            ans += c
            heapq.heappush(heap, c)
            print("heap=", heap)
            print("ans=", ans)
        return ans + heapq.heappop(heap)


if __name__ == '__main__':
    solution = Solution()
    sticks = [2, 4, 3]
    res = solution.connectSticks(sticks)
    print("res=", res)
