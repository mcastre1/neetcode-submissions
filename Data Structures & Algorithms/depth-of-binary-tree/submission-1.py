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
        # stack to keep track of seen nodes
        stack = deque()
        stack.append([root, 1])  # We will keep track of the level each node is at, we start with root being 1
        maxH = 1 # Since we have a root, we start with the maxH being 1.

        while stack:
            # When we pop we set the maxH with the current nodes level, if its greater.
            curr = stack.pop()
            maxH = max(maxH, curr[1])

            # Whenever find children nodes, we add them to the stack
            # and keep track of their level, which would be the parent's plus 1.
            if curr[0].right:
                stack.append([curr[0].right, curr[1]+1])
            if curr[0].left:
                stack.append([curr[0].left, curr[1]+1])


        return maxH