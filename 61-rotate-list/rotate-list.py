class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # Find length and tail
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        k %= n

        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail
        steps = n - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break circle
        new_tail.next = None

        return new_head