# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = head
        prev = None
        while node.next is not None:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
        node.next = prev
        return node