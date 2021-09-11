#  Copyright (c) 2021
#  @Author: xiaoweixiang
class RecentCounter:
    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        le = len(self.arr)
        index = 0
        for i in range(le):
            if self.arr[i] >= t - 3000:
                index = i
                break
        self.arr = self.arr[index:]
        return le - index

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
