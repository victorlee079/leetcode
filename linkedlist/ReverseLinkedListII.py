# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = dummy
        n = right - left + 1
        
        while right > 0:
            fast = fast.next
            right -= 1
            if left > 1:
                slow = slow.next
                left -= 1
        
        prev, curr = fast.next, slow.next
              
        for i in range(n):
            curr.next, prev, curr = prev, curr, curr.next
        
        slow.next = prev
        
        return dummy.next
    
    # Single Pass
    def reverseBetweenSp(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(next=head)
        slow = fast = dummy
        
        while left > 1:
            slow, fast = slow.next, fast.next
            right -= 1
            left -= 1
        
        prev, curr, last = None, slow.next, slow.next
              
        for i in range(right):
            curr.next, prev, curr = prev, curr, curr.next
        
        slow.next, last.next = prev, curr
        
        return dummy.next
