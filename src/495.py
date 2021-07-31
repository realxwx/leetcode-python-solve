#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] >= duration:
                ans += duration
            else:
                ans += timeSeries[i] - timeSeries[i - 1]
        return ans + duration
