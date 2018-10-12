# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def rearrangeLastN(l, n):
    origHead = l
    lastN = []
    count = 0
    removeFrom = ListNode(None)
    
    if n == 0:
        return l
    
    while l is not None:
        count += 1
        lastN.append(l)
        if len(lastN) > n:
            removeFrom = lastN.pop(0)
        l = l.next
    
    if count == n:
        return origHead
    
    lastN[n-1].next = origHead
    removeFrom.next = None
    
    return lastN[0]