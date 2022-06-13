# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getStack(head):
            stk = []
            while head:
                stk.append(head)
                head = head.next
            return stk
        
        stk1, stk2 = getStack(l1), getStack(l2)
        
        a = b = carry = 0
        res = None
        
        while stk1 or stk2 or carry:
            a = stk1.pop().val if stk1 else 0
            b = stk2.pop().val if stk2 else 0
            s = a + b + carry
            if s >= 10:
                s, carry = s-10, 1
            else:
                carry = 0
            node = ListNode(val=s, next=res)
            res = node
        
        return res
                
