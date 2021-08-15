#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections


class Solution:
    def validPalindrome(self, s: str) -> bool:
        d = dict(collections.Counter(s))
        count = 0
        for i, j in d.items():
            if j % 2 == 1:
                count += 1
        return count <= 1
