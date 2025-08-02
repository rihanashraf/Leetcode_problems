# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        difference = [float('inf')]
        prev = [None]

        def smallest(root):
            if not root:
                return

            smallest(root.left)
            if prev[0] is not None:
                difference[0] = min(difference[0], root.val - prev[0])

            prev[0] = root.val

            smallest(root.right)

        smallest(root)
        return difference[0]


            

        