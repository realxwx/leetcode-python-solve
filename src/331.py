#  Copyright (c) 2021
#  @Author: xiaoweixiang
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        想了半天，没想出来方法
        :param preorder:
        :return:
        """
        a = preorder.split(",")
        tmp = 1
        for c in a:
            tmp -= 1
            if tmp < 0:
                return False
            if c != '#':
                tmp += 2
        return tmp == 0
