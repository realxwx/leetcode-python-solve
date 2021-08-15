#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t or len(s) != len(t): return False
        ds = dict(collections.Counter(s))
        dt = dict(collections.Counter(t))
        for k, v in ds.items():
            if dt.get(k) is None or dt[k] != v:
                return False
        return True
