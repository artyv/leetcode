# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.check_path(root, head)
    
    def check_path(self, node, head):
        if not node:
            return False
        if self.dfs(node, head):
            return True
        
        return self.check_path(node.left, head) or self.check_path(node.right, head)
    
    def dfs(self, node, head):
        if not head:
            return True
        if not node:
            return False
        
        if node.val != head.val:
            return False
        return self.dfs(node.left, head.next) or self.dfs(node.right, head.next)
        
