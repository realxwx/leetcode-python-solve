#  Copyright (c) 2021
#  @Author: xiaoweixiang
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        cursor = TreeNode(0)
        head = cursor

        def inorder(ro: TreeNode):
            nonlocal cursor
            if not ro: return
            inorder(ro.left)
            cursor.right = ro
            cursor.left = None
            cursor = cursor.right
            inorder(ro.right)

        inorder(root)
        return head.right
