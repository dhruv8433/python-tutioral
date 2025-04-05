class Stack(list):
    def push(self, value):
        self.append(value)

    def pop(self):
        if not self:
            print("Stack Underflow")
            return None
        return super().pop()

    def display(self):
        print("Stack (top to bottom):")
        for item in reversed(self):
            print(item)

    def peek(self):
        if not self:
            print("Stack is empty")
            return None
        return self[-1]
    
# Testing the Stack class
st = Stack()

st.push(10)
st.push(20)
st.push(30)

st.display()

print("Popped:", st.pop())

st.display()

print("Peek:", st.peek())
