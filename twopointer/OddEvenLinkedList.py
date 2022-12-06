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
    
    def oddEvenList20220612(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head, even_head = ListNode(), ListNode()
        odd_curr, even_curr = odd_head, even_head

        i, curr = 1, head

        while curr:
            if i % 2 == 1:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            else:
                even_curr.next = curr
                even_curr = even_curr.next
            i += 1
            curr = curr.next

        odd_curr.next, even_curr.next = even_head.next, None
        return odd_head.next
