def removeKFromList(l, k):
    head = ListNode(None)
    tail = head
    
    while l is not None:
        if l.value != k:
            tail.next = l
            tail = tail.next
        l = l.next
        
    tail.next = None
    return head.next