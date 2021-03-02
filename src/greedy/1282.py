#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        a = []
        for idx, size in enumerate(groupSizes):
            a.append([idx, size])

        a.sort(key=lambda x: x[1])
        print("a=", a)
        ans = []
        while len(a) > 0:
            tmp = []
            t = a.pop()
            tmp.append(t[0])
            for _ in range(t[1]):
                tmp.append(a.pop()[0])
            ans.append(tmp)
        return ans
