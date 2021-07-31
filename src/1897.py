#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l = len(words)
        m = {}
        for s in words:
            for c in s:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
        for v in m.values():
            if v != l:
                return False
        return True
