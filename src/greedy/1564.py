#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[0:i + 1])
        j, cnt = 0, 0
        boxes.sort()
        for height in warehouse[::-1]:
            if j < len(boxes) and boxes[j] <= height:
                cnt += 1
                j += 1
        return cnt
