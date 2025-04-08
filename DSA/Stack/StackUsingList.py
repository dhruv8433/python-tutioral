class Stack:
    def __init__(self):
        self.data = []  # Use self.data to store stack elements

class StackUsingList:
    def __init__(self):
        super().__init__()  # Initialize the base class constructor

    def display(self):
        if not self.data:
            print("Stack is empty")
        else:
            print("Stack (top to bottom):")
            for i in reversed(self.data):
                print(i)

    def push(self, value):
        super
        self.data.append(value)  # Use append to push to stack

    def pop(self):
        if not self.data:
            print("Stack Underflow")
            return None
        return self.data.pop()
    
    def peek(self):
        if not self.data:
            print("Stack is empty")
            return None
        return self.data[-1]

# Example usage
st = StackUsingList()
st.push(10)
st.push(20)
st.push(30)

st.display()

print("Popped:", st.pop())
st.display()

print("Peek:", st.peek())