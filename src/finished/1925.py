#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        a = [b ** 2 for b in range(1, n + 1)]
        for i in range(1, len(a) - 2):
            for j in range(i + 1, len(a) - 1):
                for k in range(j + 1, len(a)):
                    if i + j == k:
                        cnt += 2
        return cnt
