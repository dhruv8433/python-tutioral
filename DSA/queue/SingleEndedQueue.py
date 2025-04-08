# A Queue is a linear data structure that follows the FIFO principle:

# First In, First Out — The first element inserted is the first one to be removed.

# ✅ Basic Operations in a Queue:
# Operation	Description
# enqueue()	Add element to the rear
# dequeue()	Remove element from the front
# peek()	Get the front element without removing it
# isEmpty()	Check if the queue is empty

from collections import deque

q = deque()

q.append(10)  # enqueue
q.append(20)
print("Poped element :",q.popleft())  # dequeue => 10
print(q)
print("Peeked elemnent : ", q[0]) # peek => 20
print("Is queue empty? : ", len(q) == 0) # isEmpty => False