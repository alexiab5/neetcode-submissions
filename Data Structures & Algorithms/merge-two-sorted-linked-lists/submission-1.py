# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        list3, head = None, None
        while node1 and node2:
            if node1.val <= node2.val:
                newNode = ListNode(node1.val)
                if not list3:
                    list3, head = newNode, newNode
                else:
                    list3.next = newNode
                    list3 = list3.next
                node1 = node1.next
            else:
                newNode = ListNode(node2.val)
                if not list3:
                    list3, head = newNode, newNode
                else:
                    list3.next = newNode
                    list3 = list3.next
                node2 = node2.next
        while node1:
            newNode = ListNode(node1.val)
            if not list3:
                list3, head = newNode, newNode
            else:
                list3.next = newNode
                list3 = list3.next
            node1 = node1.next
        while node2:
            newNode = ListNode(node2.val)
            if not list3:
                list3, head = newNode, newNode
            else:
                list3.next = newNode
                list3 = list3.next
            node2 = node2.next
        return head