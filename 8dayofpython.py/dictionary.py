# person = {
#     'first_name':'Anjali',
#     'last_name':'kumari',
#     'age':20,
#     'country':'india',
#     'is_marred':False,
#     'skills':['Java', 'c', 'c++', 'Python']
    
#     }
    
# print(person)
# print(len(person))
# print(person['first_name'])
# print(person['last_name'])
dog = dict()
dog = {'name':'tom', 'color':'black','breed':'black','age':2}
print(dog)
print(len(dog))
student = {'first_name':'anjali','last_name':'kumari','gender':'female','age':20,'maritalstatus':'False','skills':['c','c++','java','python'],'country':'india','city':'hajipur'}
print(student)
print(len(student))
key = student.keys()
print(key)
values = student.values()
print(values)

print(student['skills'])
print(type(student['skills']))
student['skills'].append('html')
student['skills'].append('python')
print(student['skills'])
keys = student.keys()
print(keys)
values = student.values()
print(values)
print(student.items())
student.pop('first_name')
print(student)
del student
print(student)




