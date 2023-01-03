# method overloading is one concept of polymorphism.
# it comes under the elements of oops.
# it is worked in the same method names and differnt arguments.
# Arguments different will be based on a number of arguments and types of arguments.
class area:
    def find_area(self,x='none',y='none'):
        if x!='none'and y!='none':
            print(x*y)
        elif x!='none':
            print(x*x)
        else :
            print("nothing")

obj=area()
obj.find_area()
obj.find_area(20)
obj.find_area(20,30)

# overriding function => 
# Method overriding is the method having the same name with the same arguments.
# It is implemented with inheritance also..
# It mostly used for memory reducing processes.

class a:
    def showdata(self):
        print("It is a function")
class b(a):
    def showdata(self):
        print("It is b functon")

obj1=b()
obj1.showdata()
