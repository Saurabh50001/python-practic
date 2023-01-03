#-----------------------User Define Function-----------------------------
# Function => A function is a block of statements which can be used repetitively in a program in program. It saves the time of a developer. In Python concept of function is same as in other languages.
# You can pass data, known as parameters, into a function.
# in python a function is defined using the def keyword.
# simple function :-
# function is define as "def abc():" here abc is function name.
def simplefunction():
    print("welcome to hello world")

# call 
simplefunction()

# functio with argument :-
def sumdata(a,b):
    print(a+b)
n=10
n1=20
sumdata(n,n1)

m2=30
m3=40
sumdata(m2,m3)

# default value set in argument
# if you set the both value then remove the argument valule and work on given value.
def sumdata1(c,d=5):
    print(c+d)

sumdata1(20)

# writen statement
def sum(e,f=5):
    g=e+f
    return g

p=sum(24,54)
print(p)

