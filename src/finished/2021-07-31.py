#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = set()
        for i, j in ranges:
            for k in range(i, j + 1):
                arr.add(k)

        for n in range(left, right + 1):
            if n not in arr:
                return False
        return True
