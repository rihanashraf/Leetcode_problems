# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def add(root, currsum):
            if not root:
                return False

            currsum += root.val

            if not root.right and not root.left:
                if currsum == targetSum:
                    return True

            return add(root.left, currsum) or add(root.right, currsum)

        return add(root, 0) 