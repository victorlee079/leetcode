class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev, curr = node, node.next
        while curr.next:
            prev.val = curr.val
            prev, curr = curr, curr.next
        prev.val = curr.val
        prev.next = None
        
    def deleteNodeRecur(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                return
            else:
                self.deleteNode(node.next)
