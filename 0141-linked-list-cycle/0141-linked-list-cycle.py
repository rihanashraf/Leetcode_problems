# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #using hashset

        curr = head
        s = set()

        while curr:
            if curr not in s:
                s.add(curr)
            else:
                return True
            curr = curr.next
        return False


