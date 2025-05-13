# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        while cur is not None:
            temp = cur
            accum_value = 0
            while temp.val != 0:
                accum_value += temp.val
                temp = temp.next
            cur.val = accum_value
            cur.next = temp.next
            cur = cur.next
        return head.next