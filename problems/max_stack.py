"""
Implement stack wrapper which support managing of max value in stack.
On each step we'd like to get what's the max value.
"""


class MinMaxStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def push(self, value) -> None:
        self.stack.append(value)

        # resolve with min stack
        if bool(self.min_stack) is False:
            self.min_stack.append(value)
        else:
            min_ = min(value, self.min_stack[-1])
            self.min_stack.append(min_)
        
        # resolve with max stack
        if bool(self.max_stack) is False:
            self.max_stack.append(value)
        else:
            max_ = max(value, self.max_stack[-1])
            self.max_stack.append(max_)
        return

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.max_stack.pop()
        return
    
    def max(self):
        return self.max_stack[-1] if bool(self.max_stack) is True else None
    
    def min(self):
        return self.min_stack[-1] if bool(self.min_stack) is True else None
    

stack = MinMaxStack()

stack.push(1)
stack.push(2)
stack.push(100)

print(stack.max())
print(stack.min())

stack.pop()

print(stack.max())
print(stack.min())