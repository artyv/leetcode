# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head.next

        while right is not None:
            new_node = ListNode(gcd(left.val, right.val))
            left.next = new_node
            new_node.next = right

            left = right
            right = right.next
        return head