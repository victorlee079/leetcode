class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = dummy
        fast = head
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next
        slow.next = slow.next.next if slow.next else None
        return dummy.next
