# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        #Greg's solution
        #important insight here is not the need to use a global but instead returning the boolean as the output of the function itself
        def balanced(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False

            return balanced(p.left, q.left) and balanced(p.right, q.right) # both the left and right sides need to be balanced or same
        return balanced(p,q)