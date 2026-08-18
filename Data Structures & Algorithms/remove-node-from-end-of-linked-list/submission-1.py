# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None

        # Reverse the list
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        # Iterate through reversed list and count
        reverse_head = prev
        prev_node = None
        count = 0
        while prev:
            count += 1
            if count == n:  # If we find the nth node, we check if we are at the top of the list
                if prev_node:
                    prev_node.next = prev.next
                else:        # Else we skip the current node
                    reverse_head = prev.next
            prev_node = prev
            prev=prev.next

        # We reverse the list again
        prev = None
        while reverse_head:
            temp = reverse_head.next
            reverse_head.next = prev
            prev = reverse_head
            reverse_head = temp

        # We return the reversed list, which would be in order now
        return prev

