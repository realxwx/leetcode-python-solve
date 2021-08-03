#  Copyright (c) 2021
#  @Author: xiaoweixiang
import collections
from typing import List


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        d = collections.Counter(questions)
        print("type d=", type(d))
        n = len(questions) / 2
        a = list(d.values())
        a.sort(reverse=True)
        cnt = 0
        for i in range(len(a)):
            n -= a[i]
            cnt += 1
            if n <= 0:
                break
        return cnt
