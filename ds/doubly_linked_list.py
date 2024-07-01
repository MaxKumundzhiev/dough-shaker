class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def set_head(self, value):
        # edge case empty dll
        if self.head is None:
            self.head = Node(value=value)
            self.head = self.tail
        
        
        # edge case is not empty dll
        # None <-- 10 <--> 1 <--> 2 <--> 3 --> None
        node = Node(value=value)
        node.next = self.head
        self.head.prev = node
        self.head = self.head.prev
    
        return self
    
    
    def set_tail(self, value):
        # edge case empty dll
        if self.head is None:
            self.head = Node(value=value)
            self.head = self.tail
        
        else:
            self.tail.next = Node(value=value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            
        
    def insert(self, value, target):
        current = self.head
        while current:
            if current.value != target:
                current = current.next
            else:
                current.prev.next = Node(value=value)
                current.prev.next.prev = current.prev
                current.prev = current.prev.next
                current.prev.next = current
                
        return self
    
    
    def delete(self, value):
        current = self.head
        while current.value != value:
            current = current.next
        
        current.prev.next = current.next
        current.next.prev = current.prev
        current.next, current.prev = None, None
        return self
    
    def delete_at_beginning(self):
        self.head = self.head.next
        self.head.prev = None
        return self
    
    def delete_at_end(self):
        self.tail = self.tail.prev
        self.tail.next = None
        return self