class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        p, q = headA, headB 
        while p and q and p != q :
            p, q = p.next, q.next
            if p == q :
                return q
            if not p :
                p = headB
            if not q :
                q = headA
        return p
