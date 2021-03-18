#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        n = len(s1)
        a, b = 0, 0
        cnt = 0
        for i in range(n):
            if s1[i] != s2[i]:
                cnt += 1
                if a == 0:
                    a = i
                else:
                    b = i
                if cnt == 2:
                    if s1[a] != s2[b] or s1[b] != s2[a]:
                        return False
                if cnt > 2:
                    return False
        return cnt == 0 or cnt == 2
