# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def summ(root, num):
            if not root:
                return 0
            num = num *10 + root.val

            if not root.right and not root.left:
                return num
            
            return summ(root.left, num) + summ(root.right, num)
        return summ(root, 0)