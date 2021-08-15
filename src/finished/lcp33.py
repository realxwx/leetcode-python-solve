#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        arr = -1
        b = False
        for i in range(len(vat)):
            if bucket[i] == 0:
                b = True
                arr = max(arr, vat[i])
            else:
                if vat[i] % bucket[i] == 0:
                    arr = max(arr, vat[i] // bucket[i])
                else:
                    arr = max(arr, vat[i] // bucket[i] + 1)
        print("arr=", arr)
        be = arr
        if b: return arr + 1
        for i in range(len(vat)):
            tmp = bucket.copy()
            tmp[i] += 1
            print("tmp=", tmp)
            ans = 0
            for i in range(len(vat)):
                if vat[i] % tmp[i] == 0:
                    ans = max(ans, vat[i] // tmp[i])
                else:
                    ans = max(ans, vat[i] // tmp[i] + 1)
            print("ans=", ans)
            print("arr=", arr)

            arr = min(arr, ans)
        return arr + 1 if be != arr else 0


if __name__ == '__main__':
    solution = Solution()
    bucket = [1, 3]
    vat = [6, 8]
    res = solution.storeWater(bucket, vat)
    print("res=", res)
