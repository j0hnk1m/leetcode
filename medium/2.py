class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

if not l1:
    return l2
if not l2:
    return l1
    
carry, res, head = 0, None, None

while l1 or l2:
    if l1 and l2:
        total = l1.val + l2.val + carry
        l1 = l1.next
        l2 = l2.next
    elif l1:
        total = l1.val + carry
        l1 = l1.next
    else:
        total = l2.val + carry
        l2 = l2.next

    carry = total // 10
    
    if not head:
        res = ListNode(total % 10)
        head = res
    else:
        res.next = ListNode(total % 10)
        res = res.next
            
if carry:
    res.next = ListNode(carry)

return head
