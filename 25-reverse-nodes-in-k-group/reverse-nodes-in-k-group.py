class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = dummy, dummy
        
        while count >= k:
            curr = pre.next
            nex = curr.next
            for _ in range(1, k):
                curr.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = curr.next
            pre = curr
            count -= k
        
        return dummy.next
