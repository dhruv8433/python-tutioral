class Employee:
    def __init__(self, name =None, id=None, salary=None):
        self.name = name
        self.id = id
        self.salary = salary
    def setId(self, id):
        self.id = id
    def setName(self, name):
        self.name = name
    def setSalary(self, salary):
        self.salary = salary
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
e1 = Employee("test", 1, 10000)
print(e1.getName() , " " , e1.getSalary() , " " , e1.getId())