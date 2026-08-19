"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_list = {}

        while head:
            if head not in new_list:
                new_node = Node(head.val, head.next, head.random)
                new_list[head] = new_node 
            head = head.next

        for old, new in new_list.items():
            if new.next:
                new.next = new_list[old.next]
            
            if new.random:
                new.random = new_list[old.random]

        return new_list[next(iter(new_list))]
