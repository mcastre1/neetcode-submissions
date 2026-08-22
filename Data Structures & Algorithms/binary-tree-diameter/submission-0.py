# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = deque()
        stack.append((root, False)) # We keep track of visited flag
        height = {}
        diameter = 0

        while stack:
            curr, visited = stack.pop()

            # If the current node is None, go to next iteration. These are leaf nodes.
            if not curr:
                continue

            if not visited:
                stack.append((curr, True))
                stack.append((curr.left, False))
                stack.append((curr.right, False))
            else:
                h_l = height.get(curr.left, 0)
                h_r = height.get(curr.right, 0)

                diameter = max(diameter, h_l + h_r)

                height[curr] = 1 + max(h_l, h_r)

        return diameter
        
