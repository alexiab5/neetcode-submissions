# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        val1, val2 = p.val, q.val
        currentNode = root
        while currentNode:
            if currentNode.val > val1 and currentNode.val > val2:
                currentNode = currentNode.left
            elif currentNode.val < val1 and currentNode.val < val2:
                currentNode = currentNode.right
            else:
                return currentNode