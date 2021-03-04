#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = collections.Counter(arr)
        length = len(arr)
        d1 = sorted(d.values(), reverse=True)
        cnt = 0
        res = 0
        for k in d1:
            cnt += k
            res += 1
            if cnt >= length / 2:
                return res
        return res
