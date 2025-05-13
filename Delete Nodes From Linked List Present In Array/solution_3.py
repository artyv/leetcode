# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur is not None and cur.val in nums:
            cur = cur.next
        nums = set(nums)

        new_head = cur
        last_node = cur
        cur = cur.next
        while cur is not None:
            if cur.val not in nums:
                last_node.next = cur
                last_node = cur
            cur = cur.next
        last_node.next = None
        return new_head