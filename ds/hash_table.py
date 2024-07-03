


"""
Hash Tables

Data Structure, which combines dynamic array and Doubly Linked Lists.
There is no index termin in HT, instead we work with hash functions, which maps some value to it's hashed value.

" __ " - it's called bucket

" | "  - it's called element (implemented as DLL data structure)

1   2   3   4   5   6
__  __  __  __  __  __
|       |           |
.       .           .
|
.

array = [1, 2, 3, 4]
array[1] = 10 --> [1, 10, 3, 4]

Requirements
- DLL unordered

Interface HT
- hash function
- insert
- delete
- search
"""

array = [1, 2, 3]

hash = [1, 2, 3]
"""
hash(N) = N mod 10

0   1   2   3   4 
__  __  __  __  __
N   1   N   N   N
    6   12  13  
    

(1) insert 1
    - count hash 1 hash(1) = 1
(2) insert 2
    - count hash 2 hash(2) = 2
(3) insert 3
    - count hash 3 hash(3) = 3
(4) insert 6
    - count hash 6 hash(6) = 1

"""

from uuid import uuid4

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, node: Node) -> None:
        self.head = node
        self.tail = self.head
        self.identifier = uuid4()
    
    # Time O(1) | Space O(1)
    def insert_at_head(
        self, value: int
    ):
        node = Node(value=value)
        current = self.head

        # edge case: if DLL is empty
        if not current:
            self.head = node
            self.tail = self.head
        # edge case: if DLL elements >= 1
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
        return self
    
    # Time O(1) | Space O(1)
    def insert_at_tail(
        self, value: int
    ):
        node = Node(value=value)
        current = self.tail

        # edge case: can not add element at tail if DLL empty
        if not current:
            raise AssertionError("You can add value at the tail only if DLL is not empty.")
        # edge case: if DLL elements >= 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return self
    
    def delete_at_head(
        self, value: int
    ):
        ...
    
    def delete_at_tail(
        self, value: int
    ):
        ...
    
    # Time O(n) | Space O(1)
    def search(
        self, value: int
    ) -> bool:
        current = self.head

        if not current:
            return False

        if current.next is None:
            return True if current.value == value else False

        while current:
            if current.value == value:
                return True
            else:
                current = current.next

        return False
        


class HashSet:
    def __init__(self) -> None:
        self.__length = 10
        self.buckets = [None] * self.__length
    
    def __hash(
        self, value: int
    ) -> int:
        return value % self.__length

    def insert(
        self, value: int
    ) -> None:
        key = self.__hash(value=value)

        # edge case: if bucket empty
        if not self.buckets[key]:
            self.buckets[key] = DoublyLinkedList(node=Node(value=value))
        # edge case: if bucket is not empty
        else:
            self.buckets[key] = self.buckets[key].insert_at_tail(value=value)
        return
    
    def remove(
        self, value: int
    ) -> None:
        key = self.__hash(value=value)
        
        # edge case: if bucket empty
        if not self.buckets[key]:
            raise AssertionError("No value to remove")
        # edge case: if bucket contains only 1 element
        elif self.buckets[key].head.next is not None:
            self.buckets[key] = self.buckets[key].delete_at_tail(value=value)
        # edge case: if bucket contains > 1 element
        else:
            self.buckets[key] = self.buckets[key].delete_at_head(value=value)
        return
    
    def search(
        self, value: int
    ) -> int | bool:
        key = self.__hash(value=value)
        bucket = self.buckets[key]
        return False if not bucket else bucket.search(value=value)

    def peek(self):
        for bucket in self.buckets:
            if not bucket:
                continue
            else:
                values = []
                current = bucket.head
                while current:
                    values.append(current.value)
                    current = current.next
                print([str(value) for value in values])
        return


hash_set = HashSet()
hash_set.insert(value=1)
hash_set.insert(value=2)
hash_set.insert(value=10)
hash_set.insert(value=11)
print(hash_set.search(value=10))
hash_set.peek()