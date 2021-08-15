#  Copyright (c) 2021
#  @Author: xiaoweixiang
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target: return True
        arr = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        le = len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr[j][le - i] = mat[i][j]
        print("1:" + "mat=", mat, ";arr=", arr)
        if arr == target: return True
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[j][le - i] = arr[i][j]
        print("2:" + "mat=", mat, ";arr=", arr)

        if mat == target: return True
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr[j][le - i] = mat[i][j]
        print("3:" + "mat=", mat, ";arr=", arr)

        if arr == target: return True
        return False
