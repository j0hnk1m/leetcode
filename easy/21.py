# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            else:
                dummy.next = l1
                l1 = l1.next
                dummy.next.next = l2
                l2 = l2.next
                dummy = dummy.next
            dummy = dummy.next

        if not l1:
            dummy.next = l2
        elif not l2:
            dummy.next = l1
        else:
            dummy.next = None

        return head.next
