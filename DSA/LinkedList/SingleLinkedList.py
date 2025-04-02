class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head # 1001
        while temp:
            print(temp.data, end=" -> ") # 10, 1002 | 20, 2000
            temp = temp.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head # 3 - 1 = 2
        for _ in range(pos - 1):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node.next = temp.next 
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(pos - 1):
            if not temp.next:
                print("Position out of bounds")
                return
            temp = temp.next
        if not temp.next:
            print("Position out of bounds")
            return
        temp.next = temp.next.next
        # 2 = 4
# Testing the linked list
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.traverse()  # Output: 10 -> 20 -> 30 -> None

ll.insert_at_beginning(5)
ll.traverse()  # Output: 5 -> 10 -> 20 -> 30 -> None

ll.insert_at_position(15, 2)
ll.traverse()  # Output: 5 -> 10 -> 15 -> 20 -> 30 -> None

ll.delete_at_beginning()
ll.traverse()  # Output: 10 -> 15 -> 20 -> 30 -> None

ll.delete_at_end()
ll.traverse()  # Output: 10 -> 15 -> 20 -> None

ll.delete_at_position(1)
ll.traverse()  # Output: 10 -> 20 -> None
