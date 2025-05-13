"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return [[null, null]]
        curr = head
        # Adding dummy nodes inside the original linked list
        while curr is not None:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        curr = head
        # Setting the correct random references
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        new_head = curr = head.next
        # Separating the new linked list 
        while curr.next is not None:
            curr.next = curr.next.next
            curr = curr.next

        return new_head