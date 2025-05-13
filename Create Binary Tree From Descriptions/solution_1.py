# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        unique = dict()
        childs = set()
        for node in descriptions:
            if unique.get(node[0], 0) == 0:
                unique[node[0]] = TreeNode(node[0])
            if unique.get(node[1], 0) == 0:
                unique[node[1]] = TreeNode(node[1])
            
            cur_node = unique[node[0]]
            child = unique[node[1]]
            if node[2] == 0:
                cur_node.right = child
            else:
                cur_node.left = child
            
            childs.add(child.val)
        
        for value in unique:
            if value not in childs:
                return unique[value]