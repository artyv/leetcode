# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        
        for _ in range(k):
            cur = head
            while cur.next.next is not None:
                cur = cur.next
            end = cur
            cur = cur.next
            end.next = None
            cur.next = head
            head = cur
        return head