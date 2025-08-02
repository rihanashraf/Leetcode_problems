# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        prev = [None]
        ans = [True]

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            if prev[0] is not None:
                if prev[0] >= root.val:
                    ans[0] = False

            prev[0] = root.val
            if ans[0] == True:
                dfs(root.right)

        dfs(root)
        return ans[0]
            

        