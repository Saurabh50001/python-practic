# list comprehension is an elegant way to define and create lists based on existion lists.
# list comprehension is generally more compact and faster than normal function and loops for creating list.
# syntax ---> [expression for item in list]

l=[]
for a in range(1,101):
    l.append(a)
print(l)    

# list comprehension
n=[m for m in range(1,101)]
print(n)

# filtration
n=[m for m in range(1,101) if m%2==0]
print(n)

# string list
s="hello"
d=[g for g in s]
print(s)