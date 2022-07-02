class Solution:
    def removeNthFromEnd(self, head, n):
        dummyHead = ListNode(next=head)
        slow, fast = dummyHead, head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return dummyHead.next
            
