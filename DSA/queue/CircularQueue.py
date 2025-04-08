class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size
        self.count = 0

    def enqueue(self, value):
        if(self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        # set value to self.rear position
        self.queue[self.rear] = value
        self.count += 1
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Queue is empty
        else:
            self.front = (self.front + 1) % self.size
        return value
    
    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        return self.queue[self.front]
    

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)

cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.enqueue(60)  # Queue is full

print("Queue elements:", cq.queue)  # Print the queue

print("Dequeued element:", cq.dequeue())  # Dequeue => 10
print("Dequeued element:", cq.dequeue())  # Dequeue => 20
print("Peeked element:", cq.peek())  # Peek => 30
print("Dequeued element:", cq.dequeue())  # Dequeue => 30
print("Dequeued element:", cq.dequeue())  # Dequeue => 40
print("Dequeued element:", cq.dequeue())  # Dequeue => 50

