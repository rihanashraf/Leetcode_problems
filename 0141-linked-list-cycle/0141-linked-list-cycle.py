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
        dicti = {}

        while curr:
            if curr not in dicti:
                dicti[curr] =1
            else:
                return True
            curr = curr.next
        return False


