# Polymorphism means same function name (but different signatures) being user for differrent types.
l=[10,30,20,40]
print(len(l))
s="welcome"    # there is the concept of polymorphism is that function is same but signature is different.
print(len(s))

# function overloading : function name is same and multiple output.
class ws:
    def displayinfo(self,name=''):
        print("welcome to hello world"+name)


obj=ws()
obj.displayinfo()
obj.displayinfo('Ram')


# function overriding : if 2 class function is same and inharit it to unother then the child class replace the parent function

class pk:
    def displayinfo(self):
        print("welcome to Ram house")

class iip(pk):
    def displayinfo(self):
        super().displayinfo()  # super function is used when the class of function is same 
        print("welcome to iip")

obj1=iip()
obj1.displayinfo()