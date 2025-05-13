# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        results = []
        def traverse(current_node):
            if current_node is None:
                return
            traverse(current_node.left)
            results.append(current_node.val)
            traverse(current_node.right)
        traverse(root)

        def BST(left, right):
            if left > right:
                return None
            mid = (left+right) // 2
            left_child = BST(left, mid-1)
            right_child = BST(mid+1, right)
            return TreeNode(results[mid], left_child, right_child)
        
        return BST(0, len(results)-1)



