#  Copyright (c) 2021
#  @Author: xiaoweixiang
import math
from typing import List


class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        """
        先计算全部ceil
        再根据list长度看是否可以变成target
        :param prices:
        :param target:
        :return:
        """
        total = 0
        diff = [0 for _ in range(len(prices))]
        a = 0
        for i in range(len(prices)):
            tmp = math.ceil(float(prices[i]))
            if tmp == float(prices[i]):
                a += 1
            total += tmp
            diff[i] = tmp - float(prices[i])
        k = total - target
        print("k=", k)
        if k < 0 or k > len(prices) - a:
            return "-1"
        diff.sort(reverse=True)
        count = sum(diff)
        print("type count:", type(count))
        for i in range(k):
            count -= diff[i]
            count += 1 - diff[i]
        return format(round(count, 3), '0.3f')
