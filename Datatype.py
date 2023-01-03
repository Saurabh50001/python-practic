# Number data type 
# int data type example
# "type" is inbuilt function in python to show his data type

a=5
print(a,type(a)) 

# float data type example
a=5.10
print(a,type(a)) 

# complex data type example
a=2+5j
print(a,type(a)) 

# String data type example
s='hello world'
print(s,type(s)) 

s='''hello world
this is a good platform
'''
print(s,type(s))

# List data type example
l=[10,'ws',2.5]
l[2]=10.2 
print(l,type(l))

# tupple data type example
# if there is one value then it not consider as a tupple
t=(10,'hello',2.5)
print(t,type(t))

# dictonary data type example
d={
    'course': 'bca',
    'section':'a'
}
print(d['course'])
print(d,type(d))

# Set data type example
s={10,20,20,30}
print(s,type(s))