# A Queue is a linear data structure that follows the FIFO principle:

# First In, First Out — The first element inserted is the first one to be removed.

# ✅ Basic Operations in a Queue:
# Operation	Description
# enqueue()	Add element to the rear
# dequeue()	Remove element from the front
# peek()	Get the front element without removing it
# isEmpty()	Check if the queue is empty

# Node for the linked list -> LINKED_LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Single Ended Queue
class SingleEndedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation - add to rear
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Dequeue operation - remove from front
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue became empty
            self.rear = None
        return value

    # Peek front element
    def peek(self):
        if self.front is None:
            print("Queue is Empty")
            return None
        return self.front.data

    # Display all elements
    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --- Test the SingleEndedQueue ---
q = SingleEndedQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()  # Output: 10 -> 20 -> 30 -> None

print("Dequeued:", q.dequeue())  # Output: 10
print("Front element:", q.peek())  # Output: 20

q.display()  # Output: 20 -> 30 -> None
