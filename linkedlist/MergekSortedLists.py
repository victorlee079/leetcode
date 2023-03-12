class Solution(object):
    def mergeKLists(self, lists):
        while len(lists) >= 2:
            temp, n = [], len(lists)
            for i in range(1, n, 2):
                temp.append(self.mergeTwoLists(lists[i-1], lists[i]))
            if n % 2 == 1:
                temp.append(lists[-1])
            lists = temp
        return lists[0] if lists else None

    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode()
        curr = dummyHead
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummyHead.next
