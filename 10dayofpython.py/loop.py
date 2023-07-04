# count = 0
# while count < 5:
    
#     print(count)
#     count = count + 1
# else:
#     print(count)
# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break
# count = 0
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1
# numbers = [0, 1, 2, 3, 4, 5]   
# for number in numbers: 
#     print(number)       
# language = 'Python'
# for letter in language:
#     print(letter)


# for i in range(len(language)):
#     print(language[i])
# numbers = (0, 1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)
# number =0
# for  number in range (11):
#     print(number)
# while number<=10:
#     print(number)
#     number = number+1
# number =10
# # for  number in range (10, 0,-1):
# #     print(number)
# while number>=0:
#     print(number)
#     number = number-1

# for i in range(0,7):
    
#     for j in range (0,i+1):
#         print('#')
# num = 0
# for num in range (11):
#     num = num*num
#     print(num * num , num)
# list = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for i in range(5):
#     print(list)
# n = 0
# sum = 0
# for n in range(0,101):
#      if n%2 == 0:
        
#         print('even number is',n)
#         # sum = sum + n
#         # print('sum of even is ',sum)
#      else:
#          print('odd number ',n)
#          sum = sum + n
#          print('sum of  odd is ',sum)
         
# def isPhoneNumber(text):
#     if len(text)!=12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#          return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#          return False
#     for i in range(8,12):
    #     if not text[i].isdecimal():
    #         return False
    # return True
# msg = 'call me 123-456-7891 tomorrow, or at 123-456-7891'
# fnum = False
# for i in range(len(msg)):

# print(isPhoneNumber('hello'))



# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:

# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')
# fruits_list = ['banana', 'orange', 'mango', 'lemon']    
# for fruit in fruits_list:
#     print(fruit)