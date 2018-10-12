# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def isListPalindrome(l):
    orig = l
    numbers = [] # dirty, use list instead ... >___<

    while l is not None:
        l = l.next
        numbers.append(l.value)

    numbers.reverse()

    for x in numbers:
        if x != orig.value:
            return False
        orig = orig.next
    
    return True