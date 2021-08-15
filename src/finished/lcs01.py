#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def leastMinutes(self, n: int) -> int:
        if n == 1: return 1
        step = 1
        cnt = 0
        while n / step > 2:
            cnt += 1
            step *= 2
        return cnt + 2
