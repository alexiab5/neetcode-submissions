class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0]

    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
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