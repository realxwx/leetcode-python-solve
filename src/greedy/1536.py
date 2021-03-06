#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        题意没看明白，看了官方后才明白
        :param grid:
        :return:
        """
        pikesi = [0] * len(grid)
        for i in range(len(grid)):
            for j in range(len(grid) - 1, -1, -1):
                if grid[i][j] == 1:
                    pikesi[i] = j
                    break
        ans = 0
        for i in range(len(grid)):
            k = -1
            for j in range(i, len(grid)):
                if pikesi[j] == i:
                    ans += j - i
                    k = j
                    break
            # reverse
            if k != -1:
                for j in range(k, i, -1):
                    pikesi[j], pikesi[j - 1] = pikesi[j - 1], pikesi[j]
            else:
                return -1
        return ans
