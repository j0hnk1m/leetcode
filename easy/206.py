class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next = ListNode(5)

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

# recursive
if not head or not head.next:
    return head
p = self.reverseList(head.next)
head.next.next = head
head.next = None
return p
