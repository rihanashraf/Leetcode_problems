# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        leng = 0

        while curr:
            leng +=1
            curr = curr.next
        remove = leng - n 
        curr = head
        j = 0
        if leng ==1 and remove ==0:
            return None

        while curr:
            if remove == 0:
                return curr.next
            j +=1
            if j == remove and leng !=1:
                curr.next = curr.next.next
            curr = curr.next
        return head



