# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stk = []
        while head:
            while stk and stk[-1][1] < head.val:
                ans[stk.pop()[0]] = head.val
            stk.append((len(ans), head.val))
            ans.append(0)
            head = head.next
        return ans
            
        
