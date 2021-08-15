#  Copyright (c) 2021 
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(bin(i).replace("0b", "").count('1'))
        return ans


if __name__ == '__main__':
    ll = Solution()
    n = 2
    res = ll.countBits(n)
    print("res:", res)
