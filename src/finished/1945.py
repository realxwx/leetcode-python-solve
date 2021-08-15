#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = ""
        for i in s:
            a += str(ord(i) - ord('a'))
        t = 0
        for i in range(k):
            for j in a:
                t += int(j)
            a = str(t)
        return t
