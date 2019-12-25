class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2

# using one pointer (get length first, then go to node length-n)
if not head or not head.next:
    return

dummy = ListNode(0)
dummy.next = head
p = head
length = 0
while p:
    p = p.next
    length += 1

p = dummy
for i in range(length-n):
    p = p2.next
p.next = p.next.next
return dummy.next

# using two pointers (maintaining length n gap between them)
if not head or not head.next:
    return

dummy = ListNode(0)
dummy.next = head
p1 = p2 = dummy

i = 0
while p2:
    if i >= n+1:
        p1 = p1.next
        p2 = p2.next
    else:
        p2 = p2.next
    i += 1
p1.next = p1.next.next
return dummy.next