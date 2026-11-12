class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            node1, node2 = lists[0], lists[1]
            dummy = node3 = ListNode()
            while node1 and node2:
                if node1.val <= node2.val:
                    node3.next = node1
                    node1 = node1.next
                else:
                    node3.next = node2
                    node2 = node2.next
                node3 = node3.next
            if node1:
                node3.next = node1
            if node2:
                node3.next = node2
            return dummy.next

        mid = len(lists) // 2
        return self.mergeKLists([
            self.mergeKLists(lists[:mid]),
            self.mergeKLists(lists[mid:])
        ])