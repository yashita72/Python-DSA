class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
     if self.top is None:
        print("Stack Underflow")
        return

     value = self.top.data
     self.top = self.top.next
     return value
    def peek(self):
     if self.top is None:
        return None

     return self.top.data
    def isEmpty(self):
     return self.top is None
    def display(self):
     current = self.top

     while current:
        print(current.data, end=" -> ")
        current = current.next

     print("None")
