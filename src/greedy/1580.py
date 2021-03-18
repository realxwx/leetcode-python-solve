#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        维护两个递减堆，每次去选择走左边还是右边
        把warehouse分成两个
        :param boxes: 
        :param warehouse: 
        :return: 
        """
        mi = min(warehouse)
        idx = 0
        for i in range(len(warehouse)):
            if warehouse[i] == mi:
                idx = i
                break
        a0 = warehouse[:idx + 1]
        a1 = warehouse[idx + 1:]
        a1 = a1[::-1]
        boxes.sort()
        # 准备 a0和a1
        for i in range(len(a0)):
            if i > 0:
                a0[i] = min(a0[i], a0[i - 1])
        for i in range(len(a1)):
            if i > 0:
                a1[i] = min(a1[i], a1[i - 1])
        a = a0 + a1
        a.sort()
        # 读取每个值，然后先试a0，再试a1
        j = 0
        blen = len(boxes)
        print("a0=", a0)
        print("a1=", a1)
        idx = 0
        ans = 0
        while j < blen and idx < len(a):
            if boxes[j] <= a[idx]:
                ans += 1
                j += 1
                idx += 1
            else:
                idx += 1

        return ans


if __name__ == '__main__':
    solution = Solution()

    boxes = [18, 4, 10, 7, 6, 19, 17, 9, 24, 10, 12, 20]
    warehouse = [6, 1, 5, 15, 22, 2, 15, 11, 14, 24, 22, 7, 16, 22, 4, 2, 4]
    res = solution.maxBoxesInWarehouse(boxes, warehouse)
    print("res=", res)
