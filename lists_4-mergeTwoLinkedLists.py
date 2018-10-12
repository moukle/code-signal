# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def appendRemaining(toList, fromList):
    while fromList is not None:
        toList.next = fromList
        toList = toList.next
        fromList = fromList.next
    return toList

def mergeTwoLinkedLists(l1, l2):
    resultHead = ListNode(None)
    resultTail = resultHead
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            resultTail.next = l1
            l1 = l1.next
        else:
            resultTail.next = l2
            l2 = l2.next
        resultTail = resultTail.next
        
    resultTail = appendRemaining(resultTail, l1)
    resultTail = appendRemaining(resultTail, l2)
        
    return resultHead.next