"""
Write a class, which implements queue using 2 stacks

Idea
    - introduce 2 stacks (push and pop)
    - when push (add) element to queue, always add value to push stack 
    - when pop (remove) element from queue:
        - if pop is not empty, return the last
        - if pop is empty, carry over all elements from push to pop and return the last element from pop
"""


class QueueWithTwoStacks:
    def __init__(self) -> None:
        self.__put: list = []
        self.__take: list = []
    
    def push(self, value) -> None:
        self.__put.append(value)
    
    def pop(self) -> int:
        take_is_empty = True if bool(self.__take) is False else False

        if take_is_empty is False:
            return self.__take.pop()
        else:
            # take over all the elements from push to pop and return the last from pop
            self.__take.extend(self.__put)
            self.__put = []
            return self.__take.pop()

    @property
    def put(self):
        return self.__put

    @property
    def take(self):
        return self.__take


q = QueueWithTwoStacks()

q.push(1)
q.push(2)
q.push(3)
print(q.put)
print(q.take)

q.pop()
print(q.put)
print(q.take)