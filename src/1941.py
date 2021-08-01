#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        l = list(s)
        d = collections.Counter(l)
        arr = list(d.values())
        for i in range(1, len(arr)):
            if arr[i - 1] != arr[i]:
                return False
        return True
