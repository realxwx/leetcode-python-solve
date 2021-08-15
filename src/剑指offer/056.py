#  Copyright (c) 2021
#  @Author: xiaoweixiang
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        a = []

        def inorder(ro: TreeNode):
            nonlocal a
            if not ro: return
            inorder(ro.left)
            a.append(ro.val)
            inorder(ro.right)

        inorder(root)
        i, j = 0, len(a) - 1
        while i < j:
            if a[i] + a[j] == k:
                return True
            elif a[i] + a[j] < k:
                i += 1
            else:
                j -= 1
        return False
