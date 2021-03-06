#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        Ce n'est pas un problème de cupidité, c'est un problème de recherche ligne par ligne Ah,
         référence officielle, en termes de nombres binaires, peut réduire la largeur de bande.
        :param n:
        :param reservedSeats:
        :return:
        """
        left, right, middle = 0b00001111, 0b11110000, 0b11000011
        import collections
        ma = collections.defaultdict(int)
        for k in reservedSeats:
            if 1 < k[1] < 10:
                ma[k[0]] |= (1 << (k[1] - 2))
        print("ma=", ma)
        ans = (n - len(ma)) * 2
        for r, bm in ma.items():
            if (bm | left) == left or (bm | right) == right or (bm | middle) == middle:
                ans += 1
        return ans
