#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        d = [a, b, c]
        # d.sort(reverse=True)
        d = sorted(d, reverse=True)
        print(d)
        count = 0
        while d[1] != 0:
            count += 1
            d[0] -= 1
            d[1] -= 1
            d = sorted(d, reverse=True)
            print("d=", d)
        return count


if __name__ == '__main__':
    solution = Solution()
    a = 2
    b = 4
    c = 6
    ans = solution.maximumScore(a, b, c)
    print("ans=", ans)
