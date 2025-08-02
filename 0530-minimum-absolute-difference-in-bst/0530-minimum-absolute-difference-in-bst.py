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
        difference = [float]
        store = deque()

        def smallest(root):
            if not root:
                return

            smallest(root.left)
            store.append(root.val)

            if len(store) == 2:
                diff = abs(store[1]-store[0])
                store.popleft()
                if diff < difference[0]:
                    difference[0] = diff

            smallest(root.right)

        smallest(root)
        return difference[0]


            

        