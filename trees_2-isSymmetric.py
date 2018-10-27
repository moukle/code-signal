#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    if t:
        return traversalTrees(t.left, t.right)
    else:
        return True

def traversalTrees(t1, t2):
    if t1 and t2:
        if t1.value == t2.value:
            if isLeaf(t1) and isLeaf(t2):
                return True
            if t1 and t2:
                return traversalTrees(t1.left, t2.right) and traversalTrees(t1.right, t2.left)
        else:
            return False
    elif t1 == t2:
        return True
    return False

def isLeaf(t):
    return t.left == None and t.right == None