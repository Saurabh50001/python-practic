# gatter and setter method
# getter is use to get the value of setter value.
# setter is use to set the value in the function or method and anywhere and private variable.
class student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,Id):  # name , id any thing we will take the value.
        self.__name=Id


obj=student()
obj.setname("2")
name=obj.getname()
print(name)

#--------------------------------------Encapsulation----------------------------------------------

# An objects variables should not always be directly accessiable.
# The methods can ensure the correct values are set. if an incorrect value is set, the method can return an error.
# symbole of private variable is double uncerscore(__) eg. __name="pankaj".
# private variable not accessable dirctly through object.
class teacher:
    __name="Pankaj"  # private variable
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):    # private function It is also work in the class no anywere.
        print("welcome to hello world")

obj=teacher()