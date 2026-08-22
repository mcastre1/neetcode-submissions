# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append((root, False))
        height = {}

        while stack:
            curr, visited = stack.pop()

            # Leaf node
            if not curr:
                continue

            if not visited:
                stack.append((curr, True))
                stack.append((curr.left, False))
                stack.append((curr.right, False))
            else:
                h_l = height.get(curr.left, 0)
                h_r = height.get(curr.right, 0)

                if abs(h_l - h_r) > 1:
                    return False

                height[curr] = 1 + max(h_l, h_r)
        return True