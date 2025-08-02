# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        #Greg's solution

        count = [k]
        ans = [0]

        def smallest(root):
            if not root:
                return 

            smallest(root.left)

            if count[0] ==1:
                ans[0] = root.val

            count[0] = count[0]-1
            if count[0] >= 1:
                smallest(root.right)

        smallest(root)
        return ans[0]



        