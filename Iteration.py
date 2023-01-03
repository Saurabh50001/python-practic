#Iteration of string
# based on lengh 
w="welcome to hello world"
t=len(w) # Len is a predefine function it is use to find length of string
print(t) #22
for a in range(t):
    print(a,w[a])

# reverse iterate
# first step
w="welcome to hello world"
w=w[-1::-1]
t=len(w) # Len is a predefine function it is use to find length of string
print(t) #22
for a in range(t):
    print(a,w[a])

# second step of reverse iteration 
for a in range(t-1,-1,-1):
    print(a,w[a])


# Second step of string iteration
# based on direct string 
p="welcome to hello world" # if we want to reverse it then reverse it in the starting.
for a in p:
    print(a)