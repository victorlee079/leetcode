# O(1) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cnt = 0
        
        curr = head
        # count
        while curr:
            cnt += 1
            curr = curr.next
        
        curr = head
        # Move cursor to middle
        for i in range(cnt // 2):
            curr = curr.next
            
        prev = None
        # Reverse latter half
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        # Compare
        ptr1, ptr2 = head, prev
        for i in range(cnt // 2):
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return True
