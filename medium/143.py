class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# split, reverse 2nd half, and merge - o(n) runtime, o(1) space
def splitList(root):
    slow = fast = root
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    return root, slow

def reverseList(root):
    prev = None
    cur = root
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def mergeLists(root1, root2):
    p1 = root1
    p2 = root2
    dummy = ListNode(-1)
    cur = dummy
    while p1 and p2:
        cur.next = p1
        p1 = p1.next
        cur.next.next = p2
        p2 = p2.next
        cur = cur.next.next
    if p2:
        cur.next = p2

    return dummy.next

if not head:
    return 
elif not head.next:
    return head

l1, l2 = splitList(head)
l2 = reverseList(l2)
ll = mergeLists(l1, l2)
return ll
