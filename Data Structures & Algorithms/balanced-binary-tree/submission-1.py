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

            # If current nodes hasnt been visited, we add the its children nodes to stack
            if not visited:
                stack.append((curr, True))
                stack.append((curr.left, False))
                stack.append((curr.right, False))
            else:
                # If it has been visited, we get the left and right subtrees heights
                h_l = height.get(curr.left, 0)
                h_r = height.get(curr.right, 0)

                # We check if the right and subtrees for this node differ by 1 or less only
                # if the above is not true, we return False
                if abs(h_l - h_r) > 1:
                    return False

                # We keep track of the current nodes height plus one
                # to account for the edge between this node and its parent.
                height[curr] = 1 + max(h_l, h_r)

        return True