# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iterative
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev
        return head
    
        # # recursive
        # if not head or not head.next:
        #     return head
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p
