#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict(Counter(arr1))
        ans = []
        print("d=", d)
        for i in arr2:
            cnt = d[i]
            for j in range(cnt):
                ans.append(i)
            d.pop(i)
            print("d=", d)
        tmp = []
        for i, j in d.items():
            for k in range(j):
                tmp.append(i)
        tmp.sort()
        print("ans=", ans)
        print("tmp=", tmp)
        return ans + tmp
