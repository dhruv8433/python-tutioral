class MinStack(object):

    def __init__(self):
        self.stack = []  
        self.min = []  

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # if min stack is empty or current value is less than or equal to the last min value, push it onto min stack
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        # if the popped value is the same as the last min value, pop it from min stack too
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
print("Top",param_3)
param_4 = obj.getMin()
print("Min",param_4)