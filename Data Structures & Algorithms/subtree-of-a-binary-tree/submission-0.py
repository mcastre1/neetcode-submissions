# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append(root)

        while stack:
            curr = stack.pop()
        
            if not curr:
                continue

            if curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot):
                    return True

            stack.append(curr.left)
            stack.append(curr.right)
        
        return False

    def isSameTree(self, l, r):
        stack = [(l, r)]

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