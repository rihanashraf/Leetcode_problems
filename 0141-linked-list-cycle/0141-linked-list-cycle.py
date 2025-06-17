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
        #Floyd's crazy solution
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy #fast gon point to dummy and slow to fast

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True

        return False
    

    #Time : O(n)
    #Space : O(1)


