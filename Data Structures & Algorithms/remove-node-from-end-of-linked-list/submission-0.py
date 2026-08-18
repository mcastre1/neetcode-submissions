# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        reverse_head = prev
        prev_node = None
        count = 0
        while prev:
            count += 1
            if count == n:
                print(f"found {prev.val}")
                if prev_node:
                    prev_node.next = prev.next
                else:
                    reverse_head = prev.next
            prev_node = prev
            prev=prev.next

        prev = None
        while reverse_head:
            temp = reverse_head.next
            reverse_head.next = prev
            prev = reverse_head
            reverse_head = temp

        return prev

