# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        new_head = ListNode(0)
        cur = new_head

        while list1 is not None or list2 is not None:
            if list1 is None:
                cur.next = list2
                break
            elif list2 is None:
                cur.next = list1
                break
            else:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
        
        return new_head.next