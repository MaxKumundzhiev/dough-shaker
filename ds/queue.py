"""""""""
Queue (Doubly Linked List)
"""""""""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
    
    def enqueue(self, value):
        """
        (1) 
        None <-- 1 --> None
        (2)
        None <--> 1 <--> 2 <--> 3 <--> Node --> None
                  |                      |    
                  h                      t
        (3)
        None
        """
        node = Node(value=value)
        
        # if queue is empty
        if self.head is None:
            self.head = node
            self.tail = self.head
        
        # if queue is not empty
        # add to the end of the queue 
        self.tail.next = node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        
        self.lenght += 1
        return self
        
        
    def dequeue(self):
        """
        (1) 
        None <-- 1 --> None
        (2)
        None <--> 1 --> 2 <--> 3 --> None
                        |      |    
                        h      t
        (3)
        None
        (4)
        <-- 2 <--> 3 --> None
            |      |    
            h      t
                   h
        """
        # queue is empty
        if self.head is None:
            value = None
        # queue contains only 1 element
        elif self.head.next is None:
            value = self.head.value
            self.head, self.tail = None, None
            self.lenght -= 1
        # queue contains > 2 element
        elif self.lenght > 2:
            value = self.head.value
            self.head.next.prev = None
            self.head = self.head.next
            self.lenght -= 1
        # queue contains only 2 element
        else:
            value = self.head.value
            self.head.next.prev = None
            self.head = self.head.next
            self.tail = self.head
            self.lenght -= 1
        return value
        
    def peek(self):
        return self.head.value if self.lenght >= 1 else None
      
    def list(self):
      values = []

      if self.head is None:
        return values

      current = self.head
      while current is not None:
        values.append(current.value)
        current = current.next
      return values