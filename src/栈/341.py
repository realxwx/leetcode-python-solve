#  Copyright (c) 2021
#  @Author: xiaoweixiang
from collections import deque


class NestedInteger(object):
    pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque()
        self.canNext = True
        for a in nestedList:
            if a.isInteger():
                self.q.append(a.getInteger())
            else:
                self.add(a.getList())
        # print("q:",self.q)

    def add(self, nestedList: [NestedInteger]):
        for a in nestedList:
            if a.isInteger():
                self.q.append(a.getInteger())
            else:
                self.add(a.getList())

    def next(self) -> int:
        if self.canNext:
            return self.q.popleft()

    def hasNext(self) -> bool:
        # print("len(self.q):",len(self.q))
        if len(self.q) > 0:
            self.canNext = True
        else:
            self.canNext = False
        return self.canNext
