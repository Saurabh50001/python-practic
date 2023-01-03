# JSON (JavaScript Object Notation).
# It is mainly used for strong and transferring data between the browser and the server.
# JSON is text, written with JavaScript object notation.
# Python too supports JSON with a built-in package called json.

# JSON supports mainly 6 data types:
# string
# number
# boolean 
# null 
# object
# array
import json

d={
    'course-name':'python',
    'fees': '2000'
}
f=json.dumps(d)  # dumps is use to convert the dictionaty into json format.
print(type(f))  # JSON is always in string or text format.
print(f)

#--------------------------------------------------------------------------------------------------

# Converting JSON to python Object.
p='{"cname":"python","fees":"3000","duration":"2 month"}' # json is always start with single cotation.
x=json.loads(p)
print(type(x))
print(x)

# iteration of dictionary file
for a in x:
    print(a,x[a])

#--------------------------------------->Writing & Reading json file<---------------------------------------

file=open("post.json","r") # "r" is use to read the json file and same as "w" is write the file. 
y=file.read()
finaldata=json.loads(y)
print(finaldata)

# itration of file
for k in finaldata:
    print(k,k['title'],k['userId'])  