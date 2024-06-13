
"""
- Implement Singly Linked List as a data sctructure.
- Mark each method (operation) Time and Space complexity.

Excpected operations:
- initialise (empty/non-empty)
- add element at the beginning
- add element at the end
- add element at the index
- remove element at the beginning
- remove element at the end
- remove element at the index
- search element
"""

from typing import Sequence, Self


class Node:
    def __init__(self, value: int) -> None:
        if isinstance(value, int) is not True:
            raise ValueError("only integer data type is supported")
        self.value: int = value
        self.next: Node | None = None


class SinglyLinkedList:
    def __init__(self, values: list[int] = None) -> None:
        self.head: None | Sequence[Node] = None
        if bool(values) is False:
            return
        else:
            [self.append(value=value) for value in values]
            return

    # Time O(n) | Space O(1)
    def append(self, value: int) -> Self:
        if self.head is None:
            self.head = Node(value=value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value=value)
        return self
    
    # Time O(1) | Space O(1)
    def add_at_beggining(self, value: int) -> Self:
        if self.head is None:
            self.head = Node(value=value)
        else:
            # -> 1 -> None
            # -> 1 -> 2 -> ... -> None
            rest = self.head
            # -> value -> None
            self.head = Node(value=value)
            # -> value -> rest
            self.head.next = rest
        return self
    
    # Time O(n) | Space O(1)
    def add_at_end(self, value: int) -> Self:
        if self.head is None:
            self.head = Node(value=value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value=value)
        return self

    # Time O(1) (find value O(n)) | Space O(1)
    def add_at_index(self, index: int, value: int) -> Self:
        if self.head is None and index > 0:
            raise ValueError(f"{self.__class__.__name__} is empty")
        
        if self.head is None and index == 0:
            self.head = Node(value=value)
        else:
            idx, current = 0, self.head
            while self.current is not None:
                # look up whether current.next idx == target idx
                if idx + 1 == index:
                    # -> 1 -> 2 -> 3 -> None (insert at index 1 (at node with value == 2))
                    rest = current.next               # 2 -> 3 -> None
                    current.next = Node(value=value)  # -> 1 -> InsertedValue -> None
                    current.next.next = rest          # -> 1 -> InsertedValue -> 2 -> 3 -> None
                    return self
                else:
                    idx, current = idx + 1, current.next
            raise ValueError(f"index exceeds length of {self.__class__.__name__}")

    # Time O(n) | Space O(1)
    def search(self, value: int) -> bool:
        if self.head is None:
            return False
        else:
            current = self.head
            while current.next is not None:
                if current.value == value:
                    return True
                else:
                    current = current.next 
            return False
    
    # Time O(1) | Space O(1)
    def delete_from_beginning(self) -> Self:
        if self.head is None:
            raise AssertionError
        else:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                self.head = current.next
                current.next = None
        return self
    
    # Time O(1) (traverse at end O(n)) | Space O(1)
    def delete_from_end(self) -> Self:
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        return self

    # Time O(1) (traverse at end O(n)) | Space O(1)
    def delete_at_index(self, index: int) -> Self:
        idx, current = 0, self.head
        # 1 -> 2 -> 3 -> None
        while current.next is not None:
            if idx + 1 != index:
                idx, current = idx + 1, current.next
            else:
                rest = current.next.next
                current.next.next = None
                current.next = rest
                return self
        raise ValueError(f"index exceeds lenght of {self.__class__.__name__}")
        

ssl = SinglyLinkedList(values=[1, 2, 3])