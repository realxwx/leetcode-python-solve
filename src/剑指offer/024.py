#  Copyright (c) 2021
#  @Author: xiaoweixiang
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        t = head
        while head.next:
            tt = head.next
            tt.next = t
            t = tt
            head = head.next
        return t
