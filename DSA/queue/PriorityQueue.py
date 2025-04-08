import heapq

pq = []
# add element in the priority queue with priority 1, 2, 3
# The lower the number, the higher the priority
# (1, 'DSA') has the highest priority 
heapq.heappush(pq, (2, 'Clean Code'))
heapq.heappush(pq, (1, 'DSA'))
heapq.heappush(pq, (3, 'React'))

print(heapq.heappop(pq))  # (1, 'DSA') — highest priority

print(pq)  # Remaining elements in the priority queue