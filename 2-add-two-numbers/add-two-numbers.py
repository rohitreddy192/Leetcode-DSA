# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(0)
        head = res
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + carry
            carry = sum//10
            num = sum%10
            res.next = ListNode(num)
            res = res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        if carry: res.next = ListNode(carry)
        return head.next
            
