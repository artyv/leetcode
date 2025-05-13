"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        results = []
        def traverse(current_node):
            if current_node is None:
                return
            if current_node.children:
                for child in current_node.children:
                    traverse(child)
            results.append(current_node.val)
        
        traverse(root)
        return results
        