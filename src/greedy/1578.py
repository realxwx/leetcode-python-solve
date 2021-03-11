#  Copyright (c) 2021 
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i, j = 0, 1
        n = len(s)
        ans = 0
        while i < n and j < n:
            if s[i] == s[j]:
                if cost[i] <= cost[j]:
                    ans += cost[i]
                    i = j
                    j += 1
                else:
                    ans += cost[j]
                    j += 1
            else:
                i = j
                j += 1
        return ans
