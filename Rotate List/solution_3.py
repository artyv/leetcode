# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0 or head.next is None:
            return head
        
        cur = head
        n = 1
        while cur.next is not None:
            n += 1
            cur = cur.next


        for _ in range(k % n):
            cur = head
            while cur.next.next is not None:
                cur = cur.next
            end = cur
            cur = cur.next
            end.next = None
            cur.next = head
            head = cur
        return head