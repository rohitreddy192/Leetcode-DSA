# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        dummy = ListNode()
        head = dummy
        carry, sum  = 0, 0
        while(l1 or l2):
            first = l1.val if l1 else 0
            sec = l2.val if l2 else 0
            sum = first + sec + carry
            carry = sum//10
            dummy.next = ListNode(sum%10)
            dummy = dummy.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry>0:
            dummy.next = ListNode(carry)
        return head.next