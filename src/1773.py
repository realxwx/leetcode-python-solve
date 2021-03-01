#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = 0
        if ruleKey == "color":
            idx = 1
        elif ruleKey == "name":
            idx = 2
        ans = 0
        for item in items:
            if item[idx] == ruleValue:
                ans += 1
        return ans
