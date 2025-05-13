# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if head is None:
            return [[]]
        list_length = 0
        cur = head
        while cur is not None:
            list_length += 1
            cur = cur.next

        n = list_length // k
        remainder = list_length % k

        res = [None] * k
        cur = head
        for i in range(k):
            dummy_node = ListNode(0)
            end = dummy_node

            for _ in range(n + (remainder > 0)):
                end.next = ListNode(cur.val)
                end = end.next
                cur = cur.next
            remainder -= 1
            res[i] = dummy_node.next

        return res
