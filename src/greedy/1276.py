#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        """
        先全部变成小汉堡，再看看等不等变成大汉堡
        :param tomatoSlices:
        :param cheeseSlices:
        :return:
        """
        if 4 * cheeseSlices < tomatoSlices or 2 * cheeseSlices > tomatoSlices or tomatoSlices % 2 == 1: return []
        little = cheeseSlices
        last = tomatoSlices - 2 * little
        if last // 2 > little:
            return []
        return [last // 2, little - last // 2]
