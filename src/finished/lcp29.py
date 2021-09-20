#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        layer = min(xPos, yPos, num - xPos - 1, num - yPos - 1)
        pre = 4 * (num * layer - layer ** 2) % 9
        ans = 0
        if xPos == layer:
            ans = pre + 1 + yPos - layer
        elif num - 1 - yPos == layer:
            ans = pre + 1 + (num - layer * 2 - 1) + xPos - layer
        elif num - 1 - xPos == layer:
            ans = pre + 1 + (num - layer * 2 - 1) * 2 + num - 1 - yPos - layer
        else:
            ans = pre + 1 + (num - layer * 2 - 1) * 3 + num - 1 - xPos - layer
        ans %= 9
        return ans if ans != 0 else 9
