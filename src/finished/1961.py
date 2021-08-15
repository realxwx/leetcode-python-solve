#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t = ""
        for i in words:
            if len(t) < len(s):
                t += i
            else:
                break
        return s == t
