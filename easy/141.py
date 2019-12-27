class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

nodes = {}
while head:
    if head not in nodes:
        nodes[head] = 1
    else:
        return True
    head = head.next
return False
