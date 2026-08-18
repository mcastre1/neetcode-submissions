# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        prev_node = head
        head = head.next
        prev_node.next = None
        

        while head.next:
            temp = head.next
            head.next = prev_node
            prev_node = head
            head = temp

        head.next = prev_node

        return head