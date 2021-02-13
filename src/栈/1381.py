#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.count = 0
        self.q = deque()

    def push(self, x: int) -> None:
        if self.count < self.size:
            self.count += 1
            self.q.append(x)

    def pop(self) -> int:
        if self.q:
            self.count -= 1
            return self.q.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < len(self.q):
                self.q[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
