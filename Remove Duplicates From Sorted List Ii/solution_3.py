# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        new_head, prev, current = None, None, head
        temp = current.val
        first_flag = True
        while current.next:
            if current.val != current.next.val:
                if first_flag:
                    if prev is not None:
                        prev.next = current
                        prev = current
                    else:
                        prev = current
                        new_head = current
                first_flag = True
                temp = current.next.val
            else:
                first_flag = False
            current = current.next
        if first_flag:
            if prev is not None:
                prev.next = current
            else:
                prev = current
                new_head = current
        elif prev is not None:
            prev.next = None
        return new_head
