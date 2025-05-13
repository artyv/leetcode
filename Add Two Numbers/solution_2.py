# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        tail = head
        remainder = 0
        
        while l1 is not None or l2 is not None or remainder != 0:
            d1 = l1.val if l1 is not None else 0
            d2 = l2.val if l2 is not None else 0
            
            s = d1 + d2 + remainder
            d = s % 10
            remainder = s // 10
            
            newL = ListNode(d)
            tail.next = newL
            tail = tail.next
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        r = head.next
        head.next = None
        return r