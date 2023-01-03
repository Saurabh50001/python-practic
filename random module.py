# python random randint() method
# return a number between 5 and 10 (both included):
# import random
# print(random.randint(5,10))

# return a number between 3(included) and 9(not included)
# print(random.randrange(3,9))

# python random choice() method 
# return a random element from a list:
# l = ["apple", "banana","cherry"]
# print(random.choice(l))


# randint() method
import random
n=random.randint(2,8)
print(n)

# randrange() method
n1=random.randrange(3,20)
print(n1)

# choice() method
l=[20,30,10,40,50]
lc=random.choice(l)
print(lc)

# random() function :-> Return a random float number between 0 and 1.
# shuffle() function :-> Takes a sequence and return the sequence in a random order
# uniform() function :-> Return a random float number between two given parameters.

# random() function
r= random.random()   # it will show the value between 0 to 1 randomly. 
print(r)

# shuffle() function
l=[20,30,10,40,50] 
random.shuffle(l)    # it will change the position of element randomly.
print(l)

# Uniform() function
u=random.uniform(3,10)  # it will show the float value between the given value randomly.
print(u)
