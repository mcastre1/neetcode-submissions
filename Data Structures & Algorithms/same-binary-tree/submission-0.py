# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        leftStack, rightStack = deque(), deque()
        leftStack.append(p)
        rightStack.append(q)

        while leftStack and rightStack:
            l, r = leftStack.pop(), rightStack.pop()

            if not l and r:
                return False
            if not r and l:
                return False
            if not r and not l:
                continue
            if not r.val == l.val:
                return False

            leftStack.append(l.left)
            leftStack.append(l.right)
            rightStack.append(r.left)
            rightStack.append(r.right)
        
        return True
