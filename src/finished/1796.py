#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def secondHighest(self, s: str) -> int:
        t = []
        for i in range(len(s)):
            if s[i].isdigit() and s[i] not in t:
                t.append(s[i])
        t.sort()
        return int(t[-2]) if len(t) >= 2 else -1
