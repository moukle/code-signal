#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
        return traversalTree(t, s, 0)
    
def traversalTree(t, s, sum):
    if t:
        sum += t.value
        if t.left == None and t.right == None:
            if sum == s:
                return True
            else:
                return False
        return traversalTree(t.left, s, sum) or traversalTree(t.right, s, sum)
    else:
        return False