class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        if self.size > 0:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def Pop(self):
        if not self.top:
            print("Stack is empty")
        elif not self.top.next:
            self.top = None
        self.top = self.top.next 
        self.size -= 1

    def peek(self):
        return self.top.data

    def print(self):
        temp = self.top
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print("None")
    
st = StackUsingLinkedList()
st.push(10)
st.push(20)
st.push(30)

st.print()

print("\npeek element is :", st.peek())

st.Pop()

st.print()