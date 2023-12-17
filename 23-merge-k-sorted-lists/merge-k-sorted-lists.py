class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        heap = []
        cur = ListNode()
        dummy = cur

        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        
        return dummy.next