# tuple is a ordered data type 
# it is work on index no 
# it is inmutable that means you can't change the data of tuple 
# ()
# single element can't known as tuple like a=(45)
# it store always more then one element
# it is faster then list.

t=(4,55,4,23,56,76,65)
l=len(t)
for a in range(l):
    print(a)
    print(t[a])

# second method
for a in t:
    print(a)


# Some function of tuple
# min() => it is use to minimum number
# max() => it is use to maximum value
# count() => it is use to count the value which is repete the value
# index() => it is use to show index of value
# sum() => it is use to sum the inner value , it only work on integer

# min() function
m=min(t)
print(m)

# max() function
ma=max(t)
print(ma)

# count() function
c=t.count(4)
print(c)

# index() function
i=t.index(56)
print(i)

# sum() function
s=sum(t,10)   # we add more then one value this show add 10 out of sum of t tuple.
print(s)




