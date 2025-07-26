# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_length = [0]
        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            diameter = left_height + right_height

            if diameter > max_length[0]:
                max_length[0] = diameter

            return 1 + max(left_height, right_height)
        height(root)
        return max_length[0]


        
        