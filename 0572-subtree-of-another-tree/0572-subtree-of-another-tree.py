# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def same(p, q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False
            if p.val != q.val:
                return False
            return same(p.right, q.right) and same(p.left, q.left)

        def subTree(root):
            if not root:
                return False
            if same(root, subRoot):
                return True
            return subTree(root.left) or subTree(root.right)
        return subTree(root)

        