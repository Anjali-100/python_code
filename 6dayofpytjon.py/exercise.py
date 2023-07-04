# Exercise 1
# a = int(input("input 1st number: "))
# b = int(input("input 2nd number: "))
# c = input('+ - * / // % **')
# if c == '+':
#     print("sum of two number is :", a+b)
# elif c == '-':
#     print("sub of two number is :", a-b)
# elif c == '*':
#     print("multi of two number is :", a*b)
# elif c == '/':
#     print("div of two number is :", a/b)
# elif c == '//':
#     print("floor div of two number is :", a//b)
# elif c == '%':
#     print("percantage of two number is :", a%b)
# elif c == '**':
#     print("exponent of two number is :", a**b)
# exercise 2
# import time 
# timestamp = time.strftime('%H %M %S')
# print(timestamp)
# hour = int(time.strftime('%H' ))
# minute = int(time.strftime('%M' ))
# second = int(time.strftime('%S' ))
# print(hour)
# print(minute)
# print(second)
# if hour > 6 and hour<12:
#     print("Good morning sir: ")
# elif hour > 12 and hour<4:
#     print("Good afternoon sir: ")
# elif hour > 4 and hour<12:
#     print("Good evening sir: ")
# exercise 3
# question = [ []]
# name = 'anjali'
# if len(name) >= 3:
#     name = name[1:]+ name[0]
#     print(name)
#     new_name = ''.join(name[:0],'qrt')+ name +''.join(name[5:],'qrt')
#     print(new_name)
# else:
#     rev_name = name[:: -1]
#     print(rev_name)
# if len(name) <3:
#     rev_name = name[:: -1]
#     print(rev_name)
# else:
#     print(name)
#     name = name[-1] + name[0:-1]
#     new_name = 'wrt'.join(name[0])+ name + 'qrt'.join(name[-1])

#     print(name)
# marks = [22,45,67,89,34]
# index = 0
# for mark in marks:
#     print (mark)
#     if(index == 3):
#         print("awesome")
#     index+=1
# questions = [["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create twitter","python","java","JS","php","none",3], 
# ["which language was used to create instagrm","python","french","JS","php","none",4],
# ["which language was used to create youtube","python","french","JS","php","none",4],
# ["which language was used to create whatsapp","python","french","JS","php","none",1],
# ["which language was used to create linkdin","python","french","JS","php","none",4],
# ["which language was used to create google","python","french","JS","php","none",3],
# ["which language was used to create mail","python","french","JS","php","none",1],
# ["which language was used to create pubg","python","c++","JS","php","none",2],
# ["which language was used to create freefire","python","c++","JS","php","none",2]]
# levels = [1000,2000,3000,5000,10000,20000,32000,40000,50000,100000]
# money = 0

# for i in range (len(questions)):
#     question = questions[i]
#     print( "question is",questions[i])
#     print(f"\n\nQuestion for Rs. {levels[i]}")
#     print(f"a. {question[1]}          b. {question[2]} ")
#     print(f"c. {question[3]}          d. {question[4]} ")
#     reply = int(input("Enter your answer (1 -4) or  0 to quit:\n" ))
    
#     if (reply == 0):
#      money = levels[i-1]
#      break
#     if(reply == questions[-1]):
#         print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(reply == 1):
#         money = 1000
#     elif(reply == 2):
#         money ==  2000
#     elif(reply == 3):
#         money ==  3000
#     elif(reply == 4):
#         money ==  5000
#     elif(reply == 5):
#         money ==  10000
#     elif(reply == 6):
#         money ==  20000
#     elif(reply == 7):
#         money ==  32000
#     elif(reply == 8):
#         money ==  40000
#     elif(reply == 9):
#         money ==  50000
#     elif(reply == 10):
#         money ==  100000
#     else:
#         print("worng answer")
#         break
# print(f"Your take home money is {money}")
# num = int(input('input any number'))
# fact = 1
# for i in range (1,num+1):
#     fact = fact*i
# print('factorial is ', fact)
# def func():
#     a, *b, c = ["tony","phony","pony"]
#     return "phony" in [b] or a[:]
# print(func())
# def greet_user():
#     print('hii')
#     print('welcome')
# print('start')    
# greet_user()
# print("finish")
# letter = 'hi my name is {1} and i am from {0}'
# country = "india"
# name = "anjali"
# print(letter.format(country, name))
# print({f'hi my name is {name} and i am from {country}'})

# def square(n):
#     '''takes in a number n, returns the square of n'''
#     print(n**2)
# square(19)
# print(square.__doc__)
# import this
# def fact(num):
#     if(num == 1 or num == 0):
#         return 1

#     else:
#         return num * fact(num - 1)
# print(fact(3))
# print(fact(4))
# print(fact(5))
# num = int(input('enter any number'))
# print(fact(num))
# def facb(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     return facb(n-1)+facb(n-2)
# for i in range (10):
#     print(facb(i))
# set1 = {2,4,6,2,5}
# set2 = {3.5,6,7,8,9}
# # print(set1.union(set2))
# # print(set1.intersection(set2))
# # set1.update(set2)
# # print(set1, set2)
# # set1.intersection_update(set2)
# # print(set2) 
# set1.add("anjali")
# set1.pop('anjali')
# print(set1)
# dic = {
#     "name": "anjali",
#     "age": 20,
#     "marks": 459,
#     "course": "bca"



# print(dic.keys())
# print(dic.values())
# for key in dic.keys():
#     print(f"{key} is {dic[key]}")
# print(f"dic, items()")
# a = input("enter any number: ")
# print(f'multiplication table of {a} is ')
# try:
#     for i in range (1, 11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
       
# except:
#     print("invalid input")
# print("Some imp lines of code")
# print("End of program")  
# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")
# def func1():
#     try:
#         l = [1,2,3,4,5]
#         i = int(input("enter the index:"))
#         print(l[i])
#         return l[i]
#     except:
#         print("some error occured")
#         return 0
#     finally:
#         print("i am executed")
# x = func1()
# print(x)
# a = int(input("enter any value between 5 and 9: "))
# if(a<5 or a>9):
#     raise ValueError("value should be between 5 and 9")

# questions = [["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4],
# ["which language was used to create fb","python","french","JS","php","none",4]]
# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
  
#   question = questions[i]
#   print(f"\n\nQuestion for Rs. {levels[i]}")
#   print(f"a. {question[1]}          b. {question[2]} ")
#   print(f"c. {question[3]}          d. {question[4]} ")
#   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
#   if (reply == 0):
#     money = levels[i-1]
#     break
#   if(reply == question[-1]):
#     print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(i == 4):
#       money = 10000
#     elif(i == 9):
#       money = 320000
#     elif(i == 14):
#       money = 10000000
#   else:
#     print("Wrong answer!")
#     break 

# print(f"Your take home money is {money}")
#  Day 4
# current week
# import datetime
# my_date = datetime.date.today()
# print(my_date)
# year, week_num, day_of_week = my_date.isocalendar()
# print("week" + str(week_num))


# Day 3
# measurement calculator
# rupees = float(input("please input rupees :"))
# dollars = rupees/64
# print(dollars, "Dollars")
# dollars = float(input("please input dollars :"))
# rupees = dollars*64
# print(rupees, "rupees")

# import time
# timestamp = time.strftime('%H %M %S')
# print(timestamp)
# hour = int(time.strftime('%H' ))

#



# # import random
# a = random.randint(1, 100)
# print(a)
# # Day 9
# # random quote generator
# from quote import quote
# res = quote('family',limit=1)
# print(res)
# # day 8
# # digital clock
# import time
# import pytz

# timezones = ['Europe/Amsterdam', 'Asia/Shanghai', 'America/New_York', 'Australia/Sydney', 'Africa/Cairo']

# for tz in timezones:
#     print(f"Current time in {tz}: {time.strftime('%H:%M:%S %Z %z', time.localtime(time.time()))}")
# def swap(list, list2):








 


    





   












