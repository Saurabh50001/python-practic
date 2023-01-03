
# [0:2:1]
# start [0]
# condition [2]
# increment/ Decrement [1]

# string is a sequence of characters.
# strings can be created by enclosing characters inside a single quote or double-quotes.
# triple quotes can be used represent multiple strings.
# It has indexing number
# string index no will start from 0 to n (left to right) and if we see start from last then -1 to n (right to left) 

w= "welcome to hello world" # space is also a character
print(w[6])
print(w[-3])

# slicing of string
w= "welcome to hello world" # space is also a character
print(w[0:7])
print(w[0::2]) # increment of 2

# reverse of string slicing
w= "welcome to hello world" # space is also a character
print(w[-1:-3])
print(w[-1::-2]) # increment of -2


# iteration of string

w ="welcome to hello world"
t=len(w)

