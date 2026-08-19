# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = ''
        l2_num = ''

        curr = l1
        while curr:
            l1_num = l1_num + f"{curr.val}"
            curr = curr.next

        curr = l2
        while curr:
            l2_num = l2_num + f"{curr.val}"
            curr = curr.next

        l1_num = l1_num[::-1]
        l2_num = l2_num[::-1]
        result = f"{int(l1_num) + int(l2_num)}"[::-1]

        head = ListNode(int(result[0]))
        curr = head

        for c in result[1:]:
            curr.next = ListNode(int(c))
            curr = curr.next

        return head