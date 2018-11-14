# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def kthSmallestInBST(t, k):
    return listFromTree(t, [], 0)[k-1]

def listFromTree(t, l, i):
    l.insert(i, t.value)
    if t.right is not None:
        listFromTree(t.right, l, i+1)
    if t.left is not None:
        listFromTree(t.left, l, i)
    return l