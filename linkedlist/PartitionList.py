# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        currHead = dummyHead = ListNode()
        currTail = dummyTail = ListNode()
        
        while head:
            if head.val < x:
                currHead.next = head
                currHead = currHead.next
            else:
                currTail.next = head
                currTail = currTail.next
            head = head.next
        
        currHead.next = dummyTail.next
        currTail.next = None
        return dummyHead.next
                
