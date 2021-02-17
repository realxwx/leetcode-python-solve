#  Copyright (c) 2021
#  @Author: xiaoweixiang
import heapq
from collections import Counter
from queue import PriorityQueue
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        a = Counter(barcodes)
        print("a=", a)
        ans = []
        pq = PriorityQueue()
        for i, j in a.items():
            pq.append([i, j])
        print("pq=", pq)
        while pq:
            if len(pq) >= 2:
                a = heapq.nlargest(1, pq, key=lambda x: (x[1]))
                b = heapq.nlargest(1, pq, key=lambda x: (x[1]))
                print("a=", a)
                print("b=", b)
                ans.append(a[0])
                ans.append(b[0])
                a[1] -= 1
                b[1] -= 1
                if a[1] > 0:
                    heapq.heappush(pq, a)
                if b[1] > 0:
                    heapq.heappush(pq, b)
            else:
                a = heapq.heappop(pq)
                ans.append(a[0])
        return ans


if __name__ == '__main__':
    solution = Solution()
    barcodes = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    ans = solution.rearrangeBarcodes(barcodes)
    print("ans=", ans)
