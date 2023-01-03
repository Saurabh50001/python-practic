# ----------------------------------------Module------------------------------------------------
# user define module
# file name is known as module name
# create module

# import module:-
# module1.py file1
def sum(a,b):
    c=a+b
    return c

def mul(a,b):
    c=a*b
    return c

# module2.py file2     
import module1
print(module1.sum(10,20))

print(module1.mul(30,23))

# second way to call  function through module
from module1 import sum  # for all function we use in the place of sum is *
print(sum(10,20))

# about alias 
import module1 as m
print(m.sum(23,45))
