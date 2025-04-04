class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
            if temp == self.head:
                break
        print("None")
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node # set new node address on head's previous
            new_node.prev = self.tail # set new node address on tail's next
            self.head = new_node
            self.tail.next = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.head.prev = new_node # set head's previous to new node
            self.tail.next = new_node 
            new_node.prev = self.tail # set tail's next to new node
            new_node.next = self.head
            self.tail = new_node

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if not self.head or pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:  # circular check
                print("Position out of bounds")
                return

        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return

        # Case: only one node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        # General case: more than one node
        to_delete = self.tail
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
    
    def delete_at_position(self, pos):
        if not self.head or pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:
                print("Position out of bounds")
            return  
        temp.next = temp.next.next
        temp.next.prev = temp


ll1 = DoublyCircularLinkedList()

ll1.insert_at_beginning(10) # 10 
ll1.insert_at_beginning(20) 

ll1.display() # 20 <=> 10 <=> None

ll1.insert_at_end(30) 

ll1.display() # 20 <=> 10 <=> 30 <=> None

ll1.insert_at_position(40, 2) # 20 <=> 10 <=> 40 <=> 30 <=> None

ll1.display()

ll1.delete_at_beginning() # 10 <=> 40 <=> 30 <=> None

ll1.display()

ll1.delete_at_end() # 10 <=> 40 <=> None

ll1.display()

ll1.delete_at_position(0) # 40 <=> None

ll1.display()