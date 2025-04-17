# queue using list
class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.front = 0
        self.rare = -1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.rare += 1
        

    def pop(self):
        """
        :rtype: int
        """
        temp = self.queue.pop(self.front)
        self.rare -= 1
        return temp
        

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[self.front]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.rare == -1
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(10)
obj.push(20)
param_2 = obj.pop()
print("Pop",param_2)
param_3 = obj.peek()
print("Peek",param_3)
param_4 = obj.empty()
print("Empty",param_4)