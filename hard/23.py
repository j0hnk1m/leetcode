class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
lists = [l1, l2, l3]

# brute force (creating new linked lists)
self.nodes = []
head = p = ListNode(0)
for l in lists:
    while l:
        self.nodes.append(l.val)
        l = l.next
for i in sorted(self.nodes):
    p.next = ListNode(i)
    p = p.next
return head.next

# heapq (adding all nodes to heap first, then adding them to ll)
import heapq

q = []
for i in lists:
    while i:
        q.append(i.val)
        i = i.next
heapq.heapify(q)

head = cur = ListNode(-1)
while q:
    val = heapq.heappop(q)
    cur.next = ListNode(val)
    cur = cur.next
return head.next

# heapq (pushing/popping simultaneously) - o(nlogk) runtime, o(n) space
import heapq

q = []
for i, node in enumerate(lists):
    if node:
        q.append((node.val, i))
heapq.heapify(q)

head = cur = ListNode(-1)
while q:
    val, i = heapq.heappop(q)
    cur.next = ListNode(val)
    cur = cur.next
    lists[i] = lists[i].next
    if lists[i]:
        heapq.heappush(q, (lists[i].val, i))
return head.next
