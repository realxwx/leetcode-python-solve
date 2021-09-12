#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        ans = sum(cards[0:cnt])
        if ans % 2 == 0:
            return ans
        m = -1
        for i in range(cnt - 1, -1, -1):
            if cards[i] % 2 == 1:
                m = i
                break
        n = -1
        for i in range(cnt, len(cards)):
            if cards[i] % 2 == 0:
                n = i
                break
        ans1 = 0
        if n != -1 and m != -1: ans1 = ans - cards[m] + cards[n]
        m = -1
        for i in range(cnt - 1, -1, -1):
            if cards[i] % 2 == 0:
                m = i
                break
        n = -1
        for i in range(cnt, len(cards)):
            if cards[i] % 2 == 1:
                n = i
                break
        ans2 = 0
        if n != -1 and m != -1: ans2 = ans - cards[m] + cards[n]
        return max(ans1, ans2)
