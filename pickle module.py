# The pickle module implementes a fundamental, but powerful algorithm for serializing and de-serializing a python object structure.

# Storing data type with pickle :-
# you can pickle objects with the following data types:
# Booleans,
# Integers,
# Floats,
# Complex number,
# (normal and unicode) strings,
# Tuples,
# List,
# Sets, and
# Dictionaris.

# To use pickle start by import it in python.
#                               import pickle
# Pickle has two main methods. The first one is dump, which dumps an object to a file object and the second one is load, which loads an object from a file object.

# Python pickle function :->
# dump() => This function is called to serialize an object hierarchy.
# load() => This function is called to de-serialize a data stream.

# Pickling data is done via the dump()function. It accepts data and a file onject. The dump() function then serializes the data and writes it to the file. The syntax of dump() is as follows:
# Syntax: dump(obj,file)

# dump() function
import pickle
l=[20,30,10,50,40]
file=open("pickle.txt","wb") # "wb" write binary
pickle.dump(l,file)
file.close()

# Unpickling with load()
# The load() function takes a file object, reconstruct the objicts from the pickled representation, and returns it. 
file=open("pickle.txt","rb")  # rb read binary
l=pickle.load(file)
print(l)