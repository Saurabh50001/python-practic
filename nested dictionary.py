# Nested Dictionary => Nested Dictionary means putting a dicitionay inside another dictionary.
# It's a collection of dictionaries into single dictionary.

course={
    'php':{'duration':'3 months','fees': 1500},
    'java':{'duration':'6 Months', 'fees': 2000},
    'c++':{'duration': '5 Months','fees':5000}
}
print(course)
print(course['php'])
print(course['php']['fees'])

# for iterate all data
for k,v in course.items():
    print(k,v)
    print(k,v['duration'],v['fees'])

# for update
course['java']['fees']=50000
print(course)
