class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

# hashmap
nodes = {}
while head:
    if head not in nodes:
        nodes[head] = 1
    else:
        return True
    head = head.next
return False

# two pointers (fast/slow)
if not head or not head.next:
    return False

slow = head
fast = head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
