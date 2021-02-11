#  Copyright (c) 2021
#  @Author: xiaoweixiang
class StockSpanner:
    """
    这道题和栈有啥关系呢
    记录值和比它小的个数
    """

    def __init__(self):
        from collections import deque
        self.q = deque()

    def next(self, price: int) -> int:
        if len(self.q) == 0:
            self.q.append([price, 1])
            return 1
        else:
            tmp = 1
            while len(self.q) > 0 and self.q[-1][0] <= price:
                t = self.q.pop()
                tmp += t[1]
            self.q.append([price, tmp])
            return tmp

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
