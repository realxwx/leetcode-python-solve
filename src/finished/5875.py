#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return 2 * (operations.count("++X") + operations.count("X++")) - len(operations)
