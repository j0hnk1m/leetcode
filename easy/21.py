class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


dummy = ListNode(0)
head = dummy

while l1 or l2:
    if l1 and l2:
        if l1.val >= l2.val:
            dummy.next = l2
            l2 = l2.next
        else:
            dummy.next = l1
            l1 = l1.next
    elif l1:
        dummy.next = l1
        break
    else:
        dummy.next = l2
        break
    dummy = dummy.next

return head.next
