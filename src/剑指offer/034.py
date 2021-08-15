#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            if self.cmp(words[i - 1], words[i], order):
                return False
        return True

    def cmp(self, s1: str, s2: str, order: str):
        for i in range(len(s1)):
            if i < len(s2):
                if order.index(s1[i]) > order.index(s2[i]):
                    return True
                elif order.index(s1[i]) < order.index(s2[i]):
                    return False
        if len(s1) > len(s2) and s1.index(s2) == 0: return True
        return False
