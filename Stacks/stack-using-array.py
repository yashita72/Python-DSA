class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
     if len(self.stack) == 0:
        print("Stack Underflow")
        return
     return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def peek(self):
     if len(self.stack) == 0:
        return None

     return self.stack[-1]
    def size(self):
     return len(self.stack)
    def display(self):
     print(self.stack)
   