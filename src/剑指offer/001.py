#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def divide(self, a: int, b: int) -> int:
        # if a == -2147483648 and b == -1: return int(2147483648)
        if a > 0 and b > 0:
            return a // b
        elif a > 0 and b < 0:
            return -(a // -b)
        elif a < 0 and b > 0:
            return -(-a // b)
        else:
            return -a // -b


if __name__ == '__main__':
    lfc = Solution()
    a = -2147483648
    b = -1
    c = lfc.divide(a, b)
    print("c=", c)
