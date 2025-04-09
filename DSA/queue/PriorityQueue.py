# Node class with data and priority
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

# Priority Queue class
class PriorityQueue:
    def __init__(self):
        self.front = None

    # Insert according to priority
    def enqueue(self, data, priority):
        new_node = Node(data, priority)

        # Case 1: Queue is empty OR new node has higher priority than front
        if self.front is None or self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
        else:
            # Traverse and find correct position
            temp = self.front
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    # Remove element from front (highest priority)
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        value = self.front.data
        self.front = self.front.next
        return value

    # Peek front element
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        return self.front.data, self.front.priority

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(f"[{temp.data}, p={temp.priority}]", end=" -> ")
            temp = temp.next
        print("None")

# --- Test the Priority Queue ---
pq = PriorityQueue()

pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)
pq.enqueue("Task D", 0)

pq.display()
# Output: [Task D, p=0] -> [Task B, p=1] -> [Task C, p=2] -> [Task A, p=3] -> None

print("Dequeued:", pq.dequeue())  # Task D
print("Front now:", pq.peek())    # Task B
pq.display()
