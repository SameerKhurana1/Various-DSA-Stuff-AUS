# Stack
# A LIFO (Last In First Out) data structure.
#
# Operations:
#   push   — O(1)
#   pop    — O(1)
#   peek   — O(1)
#   search — O(n)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack[::-1])


# Example
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()        # Output: [3, 2, 1]
print(s.peek())    # Output: 3
print(s.pop())     # Output: 3
s.display()        # Output: [2, 1]
