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
        glob = [True]

        def balanced(p, q):
            if not p:
                if not q:
                    return
                else:
                    glob[0] = False
                    return
            if not q:
                if not p:
                    return 
                else:
                    glob[0] = False
                    return
            if glob[0] is False:
                return 
            if p.val != q.val:
                glob[0] = False
            left = balanced(p.left, q.left)
            right = balanced(p.right, q.right)
            return 
        balanced(p,q)
        return glob[0]
        #did it myself yayyy!!!