# it is always writen in camel case(first leter of all word) and no space.
# all method is define in the class.
# function define both class and other side also.
class DemoClass:
    a=10
    def sumvalue(self): #  in the class function always work with any argument. 
        print(20+30)
demoobject=DemoClass()
demoobject1=DemoClass()
print(demoobject.a)
print(demoobject1.a)
demoobject.sumvalue()