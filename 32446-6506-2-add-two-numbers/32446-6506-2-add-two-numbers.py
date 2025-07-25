# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() #created for the new list
        curr = dummy #nodes in the new list
        carry = 0 

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit 
            val = v1+v2+carry
            carry = val//10 
            val = val%10 
            curr.next = ListNode(val) #new value inserted 

            #update ptrs
            curr = curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next
        
#come and review this later, logic understood but execution could be a bit better from my side, execution code understood just get more practice



