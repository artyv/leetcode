# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.val)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(root)
        
        def add(current_node):
            if current_node.left is not None:
                add(current_node.left)
            current_node.val += sum(results[results.index(current_node.val)+1:])
            if current_node.right is not None:
                add(current_node.right)
        add(root)
        
        return root