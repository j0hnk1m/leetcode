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

# brute force (creating new linked lists) - o(nlogn) time, o(n) space
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

# comparing one by one - o(kn) time, o(1) space
if not lists:
    return

head = cur = ListNode(0)
while True:
    minNode, i = min((val, i) for i, val in enumerate([l.val if l else float('inf') for l in lists]))
    if not lists[i]:
        break
    cur.next = lists[i]
    cur = cur.next
    lists[i] = lists[i].next
    
return head.next


# heapq (adding all nodes to heap first, then adding them to ll) - o(nlogn) time, o(n) space
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


# divide and conquer merge recursive - o(nlogk) time, o(1) space
def mergeKLists(self, lists):
    if not lists:
        return 
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists)//2
    l = self.mergeKLists(lists[:mid])
    r = self.mergeKLists(lists[mid:])
    return self.merge(l, r)

def merge(l1, l2):
    head = cur = ListNode(0)
    while l1 or l2:
        if l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        elif l1:
            cur.next = l1
            break
        else:
            cur.next = l2
            break
    return head.next

# divide and conquer merge iterative - o(nlogk) time, o(1) space
def merge(l1, l2):
    head = cur = ListNode(0)
    while l1 or l2:
        if l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        elif l1:
            cur.next = l1
            break
        else:
            cur.next = l2
            break
    return head.next

i = 1
while i < len(lists):
    for idx in range(0, len(lists)-i, i*2):
        lists[idx] = merge(lists[idx], lists[idx+i])
    i *= 2

if len(lists) == 0:
    return lists
return lists[0]