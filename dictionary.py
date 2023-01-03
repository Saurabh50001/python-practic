# Dictionary is an unordar data type
# it work on key or values, pair of key and value
# it is define as {}

from tkinter import E


d={
    'name':"python",
    'fees':8000,
    'duration': "2 months"

}
print(d)
f=d['fees']
print(f)

for n in d:
    print(n)
    print(d[n])

# Dictionary Functions
# 1. get() => get value through the keys.  
# 2. keys() => it give only keys one by one
# 3. values() => It give only value one by one
# 4. items() => It give both keys and value

# 1. get() function
p=d.get("name")
print(p)

# 2. keys() function
for a in d.keys():
    print(a)

# 3. values() function
for b in d.values():
    print(b)

# 4. items() function
for a,b in d.items():
    print(a,b)


# Some more function of Dictionary
# for delete the values of dectionary => 1. del and 2. pop()

# 1. del keyword

# del d['fees']
# print(d)

# 2. pop() function
e=d.pop('fees')
print(e)
print(d)

# dict() => it is use to cteate a new dictionary
p=dict(name='java',fees='2000')
print(p)

# update() function => it is use to update the value of dictionary.
d.update({'fees': 5000})
print(d)

# clear() function => It is use to clear all data of a dictionary.
d.clear()
print(d)

# how to insert the the new keys
d['desc']="this is python"
print(d)

