# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # dummy node before head
        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n+1):
            first = first.next

        # Move both pointers until first reaches end
        while first:
            first = first.next
            second = second.next

        # Now second is right before the node to delete
        second.next = second.next.next

        return dummy.next
