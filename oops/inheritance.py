# inheritance => it is use to transfer the function of more then one class into another class.
# It has type single , Multilevel and multiple

# single inheritance 
class A:
    def displayA(self):
        print("welcome to hello world A")
class B(A):
    def displayB(self):
        print("welcome to hello world B")
obj=B()
obj.displayA()
obj.displayB()

# multilevel inheritance 
class C:
    def displayC(self):
        print("welcome to hello world C")
class d(C):
    def displayd(self):
        print("welcome to hello world d")
class E(d):
    def displayE(self):
        print("welcome to hello world E")

obj1=E()
obj1.displayC()
obj1.displayd()
obj1.displayE()

# hybrid or multiple inheritance
class F:
    def displayF(self):
        print("How are you? F")
class G:
    def displayG(self):
        print("I am fine and you. G")
class H(F,G):
    def displayH(self):
        print("I am also fine. H")

obj2=H()
obj2.displayF()
obj2.displayG()
obj2.displayH()