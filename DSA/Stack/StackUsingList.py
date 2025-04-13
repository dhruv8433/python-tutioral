class StackUsingList:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack
        self.size = 0    # Initialize the size of the stack
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def isEmpty(self):
        return self.size == 0

    def Pop(self):
        if self.isEmpty():
            return None
        self.stack.pop(self.size - 1)  # Remove the last item (top of the stack)
        self.size -= 1

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.size - 1]
    
    def print(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            # first start, end and diff is -1
            for i in range(self.size - 1, -1, -1): # Print from top to bottom
                print(self.stack[i], end = "->")
            print("None")
    
sl = StackUsingList()
sl.push(10)
sl.push(20)
sl.push(30)

print("\npeek element is :", sl.peek())

sl.print()

sl.Pop()

print("\npeek element is :", sl.peek())

sl.print()