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
        def same(p, q):
            if not p and not q:
                return
            if not p:
                if q:
                    glob[0] = False
                    return
            if not q:
                if p:
                    glob[0] = False 
                    return 
            if glob[0] is False:
                return

            if p.val != q.val:
                glob[0] = False
                return

            right = same(p.right, q.right)
            left = same(p.left, q.left)
        same(p, q)
        return glob[0]