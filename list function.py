# count() it is use to count how many time the value repeat in the exesting list
# max() It is use to get the maximum no. of the the exesting list
# min() it is use to get the minum no. of the exestiong list
# sort() it is using for sorting and it is in accending order
# reverse() it is use to reverse the list
# index() it is use to show index no of the exexting list

l=[10,20,40,10,20,60]
# count() function
l=[10,20,40,10,20,60]
c=l.count(10)
print(c)

# max() function
l=[10,20,40,10,20,60]
a=max(l)
print(a)

p=["hello","world"]
g=max(p)
print(g)

# min() function
l=[10,20,40,10,20,60]
a=min(l)
print(a)

p=["hello","world"]
g=min(p)
print(g)

# sort() function
l=[10,20,40,10,100,20,60]
l.sort()
print(l)

# reverse() function
l=[10,20,40,10,100,20,60]
l.sort()
l.reverse()
print(l)

p=["hello","world"]
p.reverse()
print(p)

# index() function
p=["hello","world"]
a=p.index("hello")
print(a)

# iterate over 2+ lists at the same time (Zip function).

k=[10,20,30,40]
k1=[2,3,4,5]
t= len(k)

for a,b in zip(k,k1): # zip display same no. of data
    print(a,b)

for h in range(t):
    print(k[h],k1[h])

# Program to convert String to a list

# m= input("Enter the value ")
# print(m)
# o=m.split() # cut the space saperate it.
# print(o)

# for multiple input convert into list.
mn=[]
for a in range(1,5):
    mo=input("enter the value" +str(a)+":-")
    mn.append(mo)
print(mn)



