class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front == None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node
        self.size += 1


    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        elif not self.front.next:
            self.front = None
            self.rear = None     
        self.front = self.front.next
        self.size -= 1

    def print(self):
        temp = self.front
        while(temp):
            print(temp.data, end = " <- ")
            temp = temp.next
        print("None")

    def get_front(self):
        return self.front.data

    def get_rare(self):
        return self.rear.data

    def get_size(self):
        return self.size
    
qu = QueueUsingLinkedList()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)

qu.print()
print("Front element is:", qu.get_front())

qu.dequeue()
qu.print()
print("last element is:", qu.get_rare())
print("Size of queue is:", qu.get_size())        