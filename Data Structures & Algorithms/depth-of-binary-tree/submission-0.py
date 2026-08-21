# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        stack = deque()
        stack.append([root, 1])
        maxH = 1

        while stack:
            curr = stack.pop()
            maxH = max(maxH, curr[1])

            print(f"parent: {curr[0].val}")
            if curr[0].right:
                print(f"left{curr[0].right.val}")
                stack.append([curr[0].right, curr[1]+1])
            if curr[0].left:
                print(f"right{curr[0].left.val}")
                stack.append([curr[0].left, curr[1]+1])


        return maxH