# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append((p, q))

        while stack:
            x, y = stack.pop()

            if not x and not y:
                continue
            if not x or not y:
                return False
            if x.val != y.val:
                return False

            stack.append((x.left, y.left))
            stack.append((x.right, y.right))
        
        return True