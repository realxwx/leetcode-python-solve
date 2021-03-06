#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        不断的去优先获取做大的两个然后去获取
        :param a:
        :param b:
        :param c:
        :return:
        """
        arr = [[a, 'a'], [b, 'b'], [c, 'c']]
        # print("arr=", arr)
        arr.sort(reverse=True)
        ans = ""
        while arr[0][0] > 0:
            if ans and len(ans) >= 2 and ans[-1] == arr[0][1] and ans[-2] == arr[0][1]:
                if arr[1][0] > 0:
                    ans += arr[1][1]
                    arr[1][0] -= 1
                else:
                    break
            else:
                ans += arr[0][1]
                arr[0][0] -= 1
            arr.sort(reverse=True)
        return ans


if __name__ == '__main__':
    solution = Solution()
    a = 0
    b = 8
    c = 11
    res = solution.longestDiverseString(a, b, c)
    print("res=", res)
