#  Copyright (c) 2021
#  @Author: xiaoweixiang
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        print("graph=", graph)
        dis = [float('inf') for _ in range(n)]
        dis[src] = 0
        seen = {}
        pq = [(0, 0, src)]
        while pq:
            print("-----------------------")
            print("pq=", pq)
            cost, k, place = heapq.heappop(pq)
            if k > K + 1 or (k, place) in seen:
                continue
            seen[k, place] = cost
            if place == dst:
                return cost
            for v, w in graph[place]:
                if cost + w < seen.get((k + 1, v), float('inf')):
                    heapq.heappush(pq, (cost + w, k + 1, v))
        return -1


if __name__ == '__main__':
    solution = Solution()
    n = 4
    edges = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    src = 0
    dst = 3
    k = 1
    res = solution.findCheapestPrice(n, edges, src, dst, k)
    print("res=", res)
