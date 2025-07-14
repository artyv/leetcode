# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        acc = head.val
        cur = head.next
        while cur:
            acc *= 2
            acc += cur.val
            cur = cur.next
        return acc
