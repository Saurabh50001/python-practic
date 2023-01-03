
# lower() function is use to set small latter cracter of all over the paragraph 
# upper() function is use to set capital latter of all over the paragraph
# title() function is use to set capital latter of all first character of all word in a paragraph
# capitalze() function is use to set only first character of a paragraph in whole paragraph rest is same as you WriteTransport

#lower() function
w="Welcome to hello world"
n=w.lower()
print(n)

# upper() function
w= "welcome to hello world"
n=w.upper()
print(n)

# title() function
w= "welcome to hello world"
n=w.title()
print(n)

# capitalize() function
w= "welcome to hello World"
n=w.capitalize()
print(n)


# find() function is use to find index no through character of string.
# index() function is also use to find index no of character.
# isalpha() function is use to present only alphabat when all are alphabat then it print true oter then false
# isdigit() function is use to present only digit when all are digit then it print true other then false
# isalnum() function is use to present both alphabat and number when all the combination of alphabat or num then print true other then false.


# find() function
w="welcome"
print(w.find('e'))
print(w.find('e',2))
print(w.find('z')) # if there has no cracter avalival in the word which we search then it print -1 index no.

# index() function
w="welcome"
print(w.index('c'))
print(w.index('c',2))
#print(w.index('z')) # if there has no cracter avalival in the word which we search then it print error.

# isalpha() function
w="welcome"
print(w.isalpha())

w="welcome567"
print(w.isalpha())

# isdigit() function
w="5457"
print(w.isdigit())

w="welcome5457"
print(w.isdigit())

# isalnum() function
w="welcome5457"
print(w.isalnum())

w="5457"
print(w.isalnum())

w="welcome"
print(w.isalnum())

w="welcome#54@" 
print(w.isalnum()) # space is also shows false value.

# ASCII VALUES ---> Ascii value is start from 65
# Ex of axcii value -- 65 is the ascii value of A
# chr() function   this takes in an interger i and converts it to a character c, so it returens a character string.

a=65
print(chr(a))

b=66
print(chr(b))

# ord() function this takes a single unicode character(string of length 1) and return an interger.
# It is also a based on ascii values.

c="d"
print(ord(c))

print(ord("C"))

print(ord("Z"))


# format() Method ---> The format() method formats the specified value(s) and insert them inside the string's plasehloder.
# The placeholder is defined using curly brackets:{}.

w= "welcome {} to {} hello world".format("A",10)
print(w)

w= "welcome {0} to {1} hello world".format("A",10)
print(w)

w= "welcome {a} to {b} hello world".format(a=20,b=10)
print(w)

# "a:10" there is 10 show the length space of character
# ^ sign use to set center of character
# > sign use to set right side of character
# < sign use to set left side of character
w= "welcome {a:10} to {b} hello world".format(a=20,b=10)
print(w)

w= "welcome {a:^10} to {b} hello world".format(a=20,b=10)
print(w)

w= "welcome {a:<10} to {b} hello world".format(a=20,b=10)
print(w)