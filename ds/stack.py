class Node:
  def __init__(self, value):
      self.value = value
      self.next: None | Node = None


class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value) -> None:
        node = Node(value=value)
        
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return

    def pop(self):
        if self.head is None:
            value = None

        elif self.head.next is None:
            value = self.head.value  
            self.head = None
    
        else:
            value = self.head.value
            self.head = self.head.next
              
        return value

    def list(self):
      result = []

      current = self.head
      while current is not None:
          result.append(current.value)
          current = current.next

      for value in reversed(result):
          print(value, end="\n")


if __name__ == "__main__":
    stack = Stack()
    stack.list()
    stack.push(1)
    stack.push(2)
    stack.list()
    value = stack.pop()
    print(value)
    stack.list()


