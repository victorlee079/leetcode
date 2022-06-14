# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk = []
        curr = head
        while curr:
            stk.append(curr)
            curr = curr.next
        n = len(stk) // 2
        for i in range(n):
            node = stk.pop()
            if node.val != head.val:
                return False
            head = head.next

        return True

    def isPalindromeReverse(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = middle = head
        reverse = None

        # find the middle node and reverse node before middle
        while fast and fast.next:
            fast = fast.next.next
            current, middle = middle, middle.next
            current.next, reverse = reverse, current

        if fast:  # mean list has odd count nodes, need change to next.
            middle = middle.next

        # check the reverse equal the middle
        while reverse:
            if reverse.val != middle.val:
                return False
            reverse = reverse.next
            middle = middle.next

        return True
