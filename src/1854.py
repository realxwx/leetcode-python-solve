#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans = [0 for _ in range(102)]
        for i, j in logs:
            for k in range(i, j + 1):
                ans[k - 1950] += 1
        return ans.index(max(ans)) + 1950
