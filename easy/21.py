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

dummy = ListNode(-1)
cur = dummy
while l1 or l2:
    if l1 and l2:
        if l1.val >= l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
    elif l1:
        cur.next = l1
        break
    else:
        cur.next = l2
        break
    cur = cur.next
return dummy.next
