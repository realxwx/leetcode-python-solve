#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n // k > 0:
            ans += n % k
            n = n // k
        return ans + n % k
