#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        a = s.split("0")
        c = 0
        for t in a:
            if t.count("1") > 0: c += 1
            if c > 1: return False
        return c == 1
