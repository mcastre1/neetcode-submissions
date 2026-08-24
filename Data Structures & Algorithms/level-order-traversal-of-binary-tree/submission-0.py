# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque()
        stack.append((root, 0))
        result = []

        while stack:
            current, index = stack.pop()

            if not current:
                continue

            if len(result) < index + 1:
                result.append([])

            result[index].append(current.val)


            stack.append((current.right, index + 1))
            stack.append((current.left, index + 1))

        return result