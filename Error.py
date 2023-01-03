# These errors can be brodaly classified into two classes:
# syntax errors
# Logical errors(Exceptions)

# syntax error :
a=10
b=20
if a==b:     # there is syntax error that is ":"
    print("yes")
else:
    print("No")

# logical error:
print(a/0) # there Zero division error
l=[10,20,30]
print(l[5])  # there is index error