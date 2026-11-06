# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [root]
        visited = {}
        while stack:
            curr = stack[-1]
            if not curr.right and not curr.left:
                visited[curr] = 1
                stack.pop()
            else:
                if curr.right and curr.right not in visited or curr.left and curr.left not in visited:
                    if curr.right:
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)
                else:
                    hl, hr = 0, 0
                    if curr.right:
                        hr = visited[curr.right]
                    if curr.left:
                        hl = visited[curr.left]
                    if abs(hl - hr) > 1:
                        return False
                    visited[curr] = max(hl, hr) + 1
                    stack.pop()
        return True            

