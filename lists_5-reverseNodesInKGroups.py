# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseNodesInKGroups(l, k):
    head = ListNode(None)
    tail = head
    while l is not None:
        subGroupHead = None
        lBak = l
        for i in range(k):
            if l is not None:
                tmp = ListNode(l.value)
                tmp.next = subGroupHead
                subGroupHead = tmp
                l = l.next
            else:
                subGroupHead = lBak
        tail.next = subGroupHead
        
        while tail.next is not None:
            tail = tail.next
            
    return head.next