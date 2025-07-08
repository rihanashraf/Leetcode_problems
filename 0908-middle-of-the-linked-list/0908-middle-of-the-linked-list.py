# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        length = 0
        while curr:
            length +=1
            curr = curr.next
        
        curr = head
        middle_length = 0
        while curr:
            middle = curr
            if middle_length == (length/2):
                return middle
            curr = curr.next
            middle_length +=1
        




        
