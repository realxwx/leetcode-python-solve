#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        a = []
        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                md = abs(p[0] - x) + abs(p[1] - y)
                a.append([md, i])
        a.sort()
        return a[0][1] if len(a) > 0 else -1
