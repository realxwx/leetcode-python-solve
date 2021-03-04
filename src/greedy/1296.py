#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        import collections
        a = collections.Counter(nums)
        b = sorted(a)
        for n in b:
            cnt = a[n]
            if cnt > 0:
                for i in range(n + 1, n + k):
                    if a[i] >= cnt:
                        a[i] -= cnt
                    else:
                        return False
        return True


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    k = 3
    ans = solution.isPossibleDivide(nums, k)
    print("ans=", ans)
