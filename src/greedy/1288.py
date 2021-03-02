#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print("intervals=", intervals)
        left = intervals[0][0]
        right = intervals[0][1]
        ans = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= left and intervals[i][1] <= right:
                continue
            else:
                ans += 1
                left = intervals[i][0]
                right = intervals[i][1]
        return ans
