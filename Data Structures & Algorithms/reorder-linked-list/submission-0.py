# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        
        # 1. Find the size of the list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        # 2. Find the middle node (stop at index (size - 1) // 2)
        mid = 0
        curr = head
        target = (size - 1) // 2
        while mid < target:
            mid += 1
            curr = curr.next
        
        # 3. Reverse the list from after the middle node
        # Save the start of second half BEFORE severing the list
        second_half = curr.next
        curr.next = None  # Cut the first half here
        
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 4. Merge the two halves in-place
        node1 = head
        node2 = prev
        
        while node2:
            next1 = node1.next
            next2 = node2.next
            
            node1.next = node2
            node2.next = next1
            
            node1 = next1
            node2 = next2