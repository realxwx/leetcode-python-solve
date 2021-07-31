#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        k = len(sensor1)
        for i in range(len(sensor1)):
            if sensor1[i] != sensor2[i]:
                k = i
                break
        if k >= len(sensor1) - 1:
            return -1
        if sensor1[k:-1] == sensor2[k + 1:]:
            return 1
        return 2
