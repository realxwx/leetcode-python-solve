#  Copyright (c) 2021
#  @Author: xiaoweixiang
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        q = deque()
        while head is not None:
            arr.append(head.val)
            head = head.next
        ans = []
        for n in arr:
            tmp = []
            while len(q) > 0 and n > q[-1][0]:
                if q[-1][1] == 0:
                    q.pop()
                    tmp.append([n, 1])
                else:
                    tmp.append(q.pop())
            q.extend(tmp[::-1])
            q.append([n, 0])
        print("q=", q)
        for i, j in q:
            if j == 0:
                ans.append(0)
            else:
                ans.append(i)
        return ans
