class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head: # if there is no head, it means the list is empty
            self.head = new_node
        else:
            new_node.next = self.head  # new node's next location is pointed to current head location
            new_node.prev = None # new node's previous location is None as it is the first node
            self.head.prev = new_node # current head's previous location is pointed to new node
            self.head = new_node # head is now pointing to new node (New Node added to start)

    def insert_at_end(self, data):
        if not self.head: # if there is no head, it means the list is empty
            self.insert_at_beginning(data) # if the list is empty, we can use the insert_at_beginning method to add the first node
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next:
                temp = temp.next # traverse to the last node
            temp.next = new_node  # new node's next location is None (as it is the last node)
            new_node.prev = temp  # new node's previous location is pointing to the last node
            new_node.next = None
    
    def inset_on_specific_position(self, data, pos):
        if not self.head or pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(pos - 1):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node.prev = temp # main logic --
        new_node.next = temp.next # new node's next location is pointing to the next node of the current node
        temp.next = new_node
        
    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next # remove the head from the list and set next node to the head
        self.head.prev = None # set the previous location of the new head to None

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

    def delete_on_specific_position(self, position):
        if not self.head or position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        temp.next = temp.next.next
        temp.next.prev = temp

        

l1 = DoublyLinkedList()
l1.insert_at_beginning(10) 
l1.insert_at_beginning(20)

l1.insert_at_end(30)

l1.display()  # 20 <=> 10 <=> 30 <=> None

l1.insert_at_end(40)

l1.display()  # 20 <=> 10 <=> 30 <=> 40 <=> None

l1.inset_on_specific_position(50, 2)
l1.inset_on_specific_position(99, 5) # just confirm if we add element on last

l1.display()  # 20 <=> 10 <=> 50 <=> 30 <=> 40 <==> 99 <=> None

l1.delete_at_beginning() # remove the first element
l1.display()  # 10 <=> 50 <=> 30 <=> 40 <=> 99 <==> None

l1.delete_at_end() # remove the last element

l1.display()  # 10 <=> 50 <=> 30 <=> 40 <==> None

l1.delete_on_specific_position(1) # remove the second element

l1.display()  # 10 <=> 30 <=> 40 <==> None