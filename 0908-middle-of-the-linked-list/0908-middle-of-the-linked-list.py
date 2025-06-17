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
        leng = 0

        while curr:
            leng +=1
            curr = curr.next
        
        mid = leng/2 

        j =0
        curr = head
        while curr and leng !=1:
            j +=1
            if j == mid:
                return curr.next
            curr = curr.next
        return curr

        
