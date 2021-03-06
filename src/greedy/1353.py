#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Events are sorted according to the second small and the first small        :param events:
        :return:
        """
        # events.sort(reverse=True)
        events.sort()
        n = 0
        for i, j in events:
            n = max(n, i, j)
        print("events=", events)
        end = []
        ans = 0
        # events.pop()
        import heapq
        for i in range(1, n + 1):
            while events and events[0][0] == i:
                heapq.heappush(end, events.pop(0)[1])
            print("end=", end)
            while end and end[0] < i:
                heapq.heappop(end)
            if end:
                heapq.heappop(end)
                ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    events = [[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]
    res = solution.maxEvents(events)
    print("res=", res)
