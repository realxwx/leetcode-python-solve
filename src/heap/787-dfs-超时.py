#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        dfs、bfs、dijstra都可以
        :param n:
        :param flights:
        :param src:
        :param dst:
        :param K:
        :return:
        """

        def price(a: List[List[int]], b: int, c: int, d: int) -> int:
            if d < 0: return float('inf')
            # 先用dfs吧
            cost = []
            for u, v, w in flights:
                if u == b and v != c:
                    cost.append(price(a, v, c, d - 1) + w)
                elif u == b and v == c:
                    cost.append(w)
            print("cost=", cost)
            ans = float('inf')
            if cost:
                ans = min(cost)
            return ans

        answer = price(flights, src, dst, K)
        return answer if answer != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    n = 4
    edges = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    src = 0
    dst = 3
    k = 1
    res = solution.findCheapestPrice(n, edges, src, dst, k)
    print("res=", res)
