# age = int(input('enter your age: '))
# if age > 18:
#     print('You are old enough to learn to drive. ')
# elif age < 18:
#     print('You need',  18-age , 'more years  to learn  to drive. ')
# my_age = 20  
# your_age = int(input('enter your age'))   
# if my_age>your_age:
#     print('you are ', my_age-your_age ,' year older than me .')
# elif my_age<your_age:
#     print('i am ', your_age-my_age ,' year younger  than you .')
# a = int(input('enter number one : '))
# b = int(input('enter number two : '))
# if a>b:
#     print(a, 'is greater than ' ,b )

# elif a<b:
#    print(a, 'is smaller than' ,b)
# grades = int(input('input grade'))
# if grades>80 and grades<100:
#     print('A grades')
# elif grades>70 and grades<89:
#     print('B grades')
# elif grades>60 and grades<69:
#     print('C grades')
# elif grades>50 and grades<59:
#     print('D grades')
# elif grades>0 and grades<49:
#     print('F grades')
# month = input('input month')
# if month == 'september' or month == 'october' or month == 'november':
#    print('the season is Autumn')
# elif month == 'december' or month == 'january' or month == 'february':
#    print('the season is Winter')
# elif month == 'march' or month == 'april' or month == 'may':
#    print('the season is winter')
# elif month == 'june' or month == 'july' or month == 'august':
#    print('the season is Summer')
# fruits = ['banana', 'orange', 'mango', 'lemon']
# does_exist = 'banana' in fruits
# print(does_exist)
# if does_exist == False:
#     fruits[3] = 'plum'
#     print(fruits)
# else:
#     print('That fruit already exist in the list')
# user = 'James'
# access_level = 3
# if user == 'admin' or access_level >= 4:
#         print('Access granted!')
# else:
#     print('Access denied!')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# skills= ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# if 'skills' in person:
#       mid_skill = skills[3]
#       print(mid_skill)
# else:
#       print('skills key is not in list item')    

# if 'skills' in person or skills == 'python':
#       print('python in skills')
# if 'skills' in person or skills == 'JavaScript' and  skills == 'React':
#       print('She is a frontend devloper')     
# elif 'skills' in person or skills == 'Node' and skills == 'Python' and skills == 'MondoDB':
#     print('He is a backend developer')
# elif  'skills' in person or skills == 'React'and skills == 'Node' and skills == 'MongoDB':
#     print('He is a fullstack developer')
# else: 
#     print('unknown title')  
if 'is_married' in person or 'is_married' == True or  'country'in person or 'country'== 'Finland':
     print('Asabeneh Yetayeh lives in Finland. He is married.')

    


