class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists: List[Optional[ListNode]], s: int, e: int) -> Optional[ListNode]:
        if s == e:
            return lists[s]
        if s < e:
            mid = (s + e) // 2
            l1 = self.partition(lists, s, mid)
            l2 = self.partition(lists, mid + 1, e)
            return self.merge(l1, l2)
        return None

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
