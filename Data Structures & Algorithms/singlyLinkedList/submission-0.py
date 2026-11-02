class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        current = self.head
        i = 0
        while current is not None and i < index:
            current = current.next
            i += 1
        if current is None or i != index:
            return -1
        return current.value

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        i = 0
        prev = self.head
        while prev is not None and i < index - 1:
            prev = prev.next
            i += 1
        if prev is None or prev.next is None:
            return False
        if prev.next == self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        current = self.head
        while current is not None:
            vals.append(current.value)
            current = current.next
        return vals