# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def getNumber(a):
    number = str(a.value)
    
    while a.next is not None:
        a = a.next
        tmp = str(a.value)
        while len(tmp) != 4:
            tmp = '0' + tmp
        number += tmp
    
    return number
    
def addTwoHugeNumbers(a, b):
    number1 = getNumber(a)
    number2 = getNumber(b)
        
    result = int(number1) + int(number2)
    result = str(result)

    pointer = None
    while len(result) > 0:
        tmp = int(result[-4:])
        result = result[:-4]
        item = ListNode(int(tmp))
        item.next = pointer
        pointer = item
    return item