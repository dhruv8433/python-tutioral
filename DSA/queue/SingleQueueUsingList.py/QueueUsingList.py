class QueueUsingList:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        self.queue.append(data)
        self.rear += 1
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        self.queue.pop(self.front)
        self.size -= 1
        self.rear -= 1

    def print(self):
        for i in range(len(self.queue)):
            print(self.queue[i], end=" <- ")
        print("None")

    def get_size(self):
        return self.size

qu = QueueUsingList()

qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)

qu.print()

print("\nDequeueing...")
qu.dequeue()

qu.print()

print("\nSize of queue:", qu.get_size())