#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx_a = idx_b = 0
        length = len(pushed)
        while idx_a < length and idx_b < length:
            if pushed[idx_a] != popped[idx_b]:
                if stack and stack[-1] == popped[idx_b]:
                    stack.pop()
                    idx_b += 1
                else:
                    stack.append(pushed[idx_a])
                    idx_a += 1
            else:
                idx_a += 1
                idx_b += 1
            if idx_a == length:
                print(stack)
                print(popped[idx_b:][::-1])
                return stack == popped[idx_b:][::-1]
        return True


if __name__ == '__main__':
    solution = Solution()
    pushed = [2, 1, 0]
    popped = [1, 2, 0]
    res = solution.validateStackSequences(pushed, popped)
    print("res:", res)
