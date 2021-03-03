class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            raise PopError("Pop from empty stack.")

    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            raise IndexError("Stack is empty.")