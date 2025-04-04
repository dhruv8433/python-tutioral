class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" => ")
            temp = temp.next
            if temp == self.head:
                break
        print("None")

    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, data, position):
        if not self.head and position > 0:
            print("Invalid position, list is empty")
        if position == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next
                if temp == self.head:  # circular check
                    print("Position out of bounds")
                    return
            next_node = temp.next
            temp.next = new_node
            new_node.next = next_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
        else:
            new_head = self.head.next
            self.head = new_head
            self.tail.next = new_head

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = self.head
                self.tail = temp
                self.tail.next = self.head

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty")
            return
        if position == 0:
            self.delete_at_beginning()
        else:
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next
                if temp == self.head:  # circular check
                    print("Position out of bounds")
                    return
            next_node = temp.next.next
            temp.next = next_node
            if temp.next == self.head:  # last node
                self.tail = temp
            


cl1 = CircularLinkedList()

cl1.insert_at_beginning(10)
cl1.insert_at_beginning(5)

cl1.display() # 5 => 10 => None

cl1.insert_at_end(20)

cl1.display() # 5 => 10 => 20 => None

cl1.insert_at_position(15, 2)

cl1.display() # 5 => 10 => 15 => 20 => None

cl1.delete_at_beginning()

cl1.display() # 10 => 15 => 20 => None

cl1.delete_at_end()

cl1.display() # 10 => 15 => None

cl1.delete_at_position(1)

cl1.display() # 10 => None