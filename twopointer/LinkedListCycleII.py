class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast:
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            slow = slow.next
            if slow == fast:
                break
                
        if fast is None:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
