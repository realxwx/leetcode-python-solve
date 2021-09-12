#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        m = {}
        print("type m=", type(m))
        for i in range(len(source)):
            for j in range(len(source[0])):
                print("source[i][j]", source[i][j])
                if m.get(source[i][j]) is None:
                    m[source[i][j]] = 1
                else:
                    m[source[i][j]] += 1
        arr = m.keys()
        print("type arr=", type(arr))
        for i in range(len(target)):
            for j in range(len(target[0])):
                if target[i][j] in arr and m[target[i][j]] > 0:
                    m[target[i][j]] -= 1
        cnt = 0
        for k, v in m.items():
            if v != 0:
                cnt += v
        return cnt


if __name__ == '__main__':
    s = Solution()
    source = [[1, 3], [5, 4]]
    target = [[3, 1], [5, 4]]
    ans = s.minimumSwitchingTimes(source, target)
    print("ans=", ans)
