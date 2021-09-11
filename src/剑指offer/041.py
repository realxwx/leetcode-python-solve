#  Copyright (c) 2021
#  @Author: xiaoweixiang
import numpy as np


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.arr = []

    def next(self, val: int) -> float:
        if len(self.arr) < self.size:
            self.arr.append(val)
            print("mean=", np.mean(self.arr))
            print("avg=", np.average(self.arr))
            return np.average(self.arr)
        else:
            self.arr = self.arr[1:]
            self.arr.append(val)
            print("mean=", np.mean(self.arr))
            print("avg=", np.average(self.arr))
            return np.average(self.arr)

        # Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
