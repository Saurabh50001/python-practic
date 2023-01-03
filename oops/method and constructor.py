class DemoClass:
    a=10
# constructor define
# constructor is automatically call when make a object , its not waiting for call it.
    def __init__(self): # Constructor is define with __init__.
        print("welcome to helloworld")

# make method       
    def showvalue(self): 
        print(self.a)   # when we use the variable in the function then first take the permossion of self.
        self.c=self.a*self.a
        print(self.c)
    
    def showvalue1(self):
        print("welcome to hello world")

    def showvalue2(self,a,b):
        print(a+b)

obj=DemoClass()
obj.showvalue()
obj.showvalue1()
obj.showvalue2(20,30)