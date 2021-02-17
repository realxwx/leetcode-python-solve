#  Copyright (c) 2021
#  @Author: xiaoweixiang
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        dfs超时，用贪心策略
        :param heights:
        :param bricks:
        :param ladders:
        :return:
        """
        if len(heights) == 1: return 0
        pq = []
        for i in range(1, len(heights)):
            dif = heights[i] - heights[i - 1]
            if dif > 0:
                heapq.heappush(pq, dif)
                if ladders == 0:
                    bricks -= heapq.heappop(pq)
                    if bricks < 0:
                        return i - 1
                else:
                    ladders -= 1
        return len(heights) - 1
