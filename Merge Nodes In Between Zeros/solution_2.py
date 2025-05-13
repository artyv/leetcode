# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        cur = head.next
        accum_value = 0
        while cur is not None:
            if cur.val != 0:
                accum_value += cur.val
            else:
                new_node = ListNode(accum_value)
                accum_value = 0
                if new_head is None:
                    new_head = new_node
                    head.next = new_head
                else:
                    new_head.next = new_node
                    new_head = new_head.next
            cur = cur.next
        return head.next