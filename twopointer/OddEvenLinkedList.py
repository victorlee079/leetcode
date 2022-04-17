# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first, second = head, head.next
        dummy = ListNode(next=second)
        
        i = 1
        curr = second.next if second.next else None
        while curr:
            if i % 2 == 0:
                second.next = curr
                second = second.next
            else:
                first.next = curr
                first = first.next
            curr = curr.next
            i += 1
                
        first.next = dummy.next
        second.next = None
        return head
