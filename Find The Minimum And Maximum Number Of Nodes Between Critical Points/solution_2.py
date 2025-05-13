# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head; cur = head.next
        crit = []
        index = 1
        while cur.next is not None:
            if cur.val > prev.val and cur.val > cur.next.val or cur.val < prev.val and cur.val < cur.next.val:
                crit.append(index)
            cur = cur.next
            index += 1
        if len(crit) <= 1:
            return [-1, -1]
        else:
            return [min(crit[i+1]-crit[i] for i in range(len(crit)-1)), crit[-1]-crit[0]]