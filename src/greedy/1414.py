#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a = 1
        b = 1
        fi = [a, b]
        while fi[-1] + fi[-2] <= k:
            fi.append(fi[-1] + fi[-2])
        print("fi=", fi)
        if fi[-1] == k: return 1
        return self.findMinFibonacciNumbers(k - fi[-1]) + 1


if __name__ == '__main__':
    solution = Solution()
    k = 645157245
    res = solution.findMinFibonacciNumbers(k)
    print("res=", res)
