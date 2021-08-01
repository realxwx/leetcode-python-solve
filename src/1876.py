#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        cnt = 0
        for i in range(len(s) - 2):
            a = s[i:i + 3]
            if a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
                cnt += 1
        return cnt
