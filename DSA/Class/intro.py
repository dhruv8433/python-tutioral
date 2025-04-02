class Test:
    x =10 

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def myFun():
        print("Hello World")

    @classmethod
    def another(cls):
        print("Hello World", cls.x)

t1 = Test(10, 20)
t2 = Test(20, 50)
print(t1.a, t1.b)
print(t2.a, t2.b)

# static method can be called using class name or object name
Test.myFun() 

t1.another()

