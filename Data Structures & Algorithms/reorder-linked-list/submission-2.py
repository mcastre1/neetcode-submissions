# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return None

        l1 = head
        slow = head
        fast = head
        mid = None
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev.next = None 
        l2 = mid

        prev_node = None
        while l2:
            temp = l2.next
            l2.next = prev_node
            prev_node = l2
            l2 = temp

        l2 = prev_node
        
        last_node = None
        while l1:
            l1_next = l1.next
            l2_next = l2.next
         
            l1.next = l2
            last_node = l2
            l2.next = l1_next
            
            l1 = l1_next
            l2 = l2_next

        last_node.next = l2

        return l1


        