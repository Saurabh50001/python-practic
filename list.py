# [0:2:1]
# start [0]
# condition [2]
# increment/ Decrement [1]


# list is a mutable value
# []
# It store multiple value

l=[1,3,5,4,6,7]
print(l)

# nested list
p=[3,5,5,8,[5,7,5,4]] 
print(p[4][2])

# mixed list
li=[2,4,"hello",[3,5,5]]
print(li[2]) # slising of list
print(li[0:2]) # two argument
print(li[1:])

# Tripal argument
pk=[1,2,3,4,5,6]
print(pk[0::2]) 
print(pk[-1::-1]) # Reverse

# itteration of list
pp=[9,10,11,12,13]
# 1st step of itteration list
t=len(pp)
for n in range(t):
    print(pp[n])

# 2nd step of itterate list
for a in pp:
    print(a)

# Reverse list itteration
for n in range(t-1,-1,-1):
    print(pp[n])

# function for delete element from list-
# del
# pop()
# remove()
# clear()

py=[10,20,30,40,50,60]
print(py)

# del function
del py[2]
print(py)

# pop() function
py.pop(2)
print(py)

print(py.pop(2)) # it is use to print deleted value also
print(py)

# Remove() function 
py.remove(60) # it work on  values
print(py)

# clear() function
py.clear() # it clear all list
print(py)

# update function of list 
# insert() it is use to insert any position.
# append() it is use add in the last of the list
# extends() it work on the inner values 

pa=[20,30,50,60,80]
print(pa)

pa[0]=10
print(pa)

# insert() function
pa.insert(0,20) # 0 is position and 20 is value
print(pa)

# append() function
n=[3,5]
pa.append(n)
print(pa) # It add as it is in  the given value

# extends() function
n=[3,5]
pa.extend(n)
print(pa)

