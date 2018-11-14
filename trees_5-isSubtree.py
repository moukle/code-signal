#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def isSubtree(t1, t2):
    if t2 == None:
        return True
    return subTree(t1,t2)

def subTree(t1, t2):
    if t1 and t2:
        if t1.value == t2.value:
            return subTree(t1.left, t2.left) and subTree(t1.right, t2.right)
        else:
            print(str(t2.value))
            return subTree(t1.left, t2) or subTree(t1.right, t2)
    elif not t1 and not t2:
        return True
    return False