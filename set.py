# set is a unorder data type or unindex 
# we can add or delete the data of set
# set is always store unique value
# set is define as {} 
# it is mutable.

# functions of sets :-
# set() => it is use convert the list or tuple value into the set.
# add() => it is use to add a new element in the set. 
# pop() => it is use to delete rendemaly element in set.
# remove() => it is also delete the inner element of set.
    # note => if the item to remove does not exist, remove() will rise an error.
# clear() => it is use to clear whole set but it print in the form of set().
# discard() => it is also delete the inner element of set.
    # note => if the item to remove does not exist, discard() will not raise an error.
# update() => it is use to update the value not change the element.

s={23,34,65,45,76}
print(s)

for a in s:
    print(a)

# set() function
l=[30,45,56,76,12]
p=set(l)
print(p)

# remove() function
s.remove(23)
print(s)

# discard() function
s.discard(65)
print(s)

# pop() function
print(p.pop())
print(p)

# clear() function
p.clear()
print(p)

# add() function
p.add(60)
print(p)

# update() function
k=[12,45,76,30]
s.update(k)
print(s)
