from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        看了其他人的解题才知道用二分
        :param nums:
        :param maxOperations:
        :return:
        """

        def canSatisify() -> bool:
            n = 0
            for num in nums:
                n += int(num / mid)
                if num % mid == 0:
                    n -= 1
            return n <= maxOperations

        left = 1
        right = 1e9
        while left <= right:
            mid = int((left + right) / 2)
            if canSatisify():
                right = mid - 1
            else:
                left = mid + 1
        return left
