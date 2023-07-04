# def weight_of_object (mass, gravity = 9.81):
#     weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
# print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon

# def add_two_number(num1,num2):
#     # total = num1+num2
#     return total
# print(add_two_number(10,15))
# def area_of_circle(r):
#     pi = 3.14
#     area = pi*r*r
#     return area
# print(area_of_circle(10))
# def add_all_nums(*nums):
#     total=0
#     for num in nums:
#         total+=num
#         if type(num) == list:
#             return 0
#     else:
#         return total
    
# print(add_all_nums(2,4,5,10))
# def check_season(month):
#     season1 = 'autumn'
#     season2 = 'winter'
#     season3 = 'spring'
#     season4 = 'summer'
#     season =''
#     if month == 'september' and  'october' and 'november':
#         season = season1
#         # return season 
        
        
#     elif month == 'december' and 'january' and  'feburary':
#         season = season2
#         # return season
        
#     elif month == 'march' and  'april' and 'may':
#         season = season3
#         # return season
        
#     elif month == 'june' and  'july' and  'august':
#         season = season4
#         # return season
        
#     return season
# print(check_season('december'))
# list = [1,2,3,4,5,6,7]
# def revese_list(l):
    
#      for i in range(-1,len(l),-1 ):
#         print(l[i])
        
#      return l
# print(revese_list([1,2,3,4,5,6,7]))
    
# def calculate_slope(x1,x2,y1,y2):
#     m = (y2-y1)/(x2-x1)
   
#     return m
# print(calculate_slope(5,15,10,15))
# def solve_quadratic_eqn(a,b,c):
#     d = b*b-4*a*c
#     if d>0:
#         print('root are real')
#     elif d==0:
#         print('root are equal')
#     elif d<0:
#         print('root are imaginary')
#     return d
# print(solve_quadratic_eqn(2,4,4))
# def print_list(list):
#     list = [1, 2, 3, 4, 5]
#     return list
# print(print_list(list))
# def capitalize_list(list):
#     list = 'anjali'
#     print(list.capitalize())
#     return list
# print(capitalize_list('anjali'))
# def add_item(food_staff,numbers):

#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     food = food_staff.append('Meat')
     
     
#     numbers = [2, 3, 7, 9]
#     number = numbers.append(5)

#     return food_staff , numbers
# print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'],[2, 3, 7, 9])) 

    
# def remove_item(food_staff):
#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     food = food_staff.remove('Milk')
#     return food_staff
# print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk']))
# def sum(number):
#     total = 0
#     for i in range(number+1):
#         total = total+i
#     return total
# print(sum(5))
# print(sum(10))
# print(sum(50))
# print(sum(100))
# def sum_of_odd(num):
#     total = 0
#     for num in range(0,num+1):
#         if num%2 == 1:
#             total = total+num
#     return total
# print(sum_of_odd(5))
# def sum_of_even(num):
#     total = 0
#     for num in range(0,num+1):
#         if num%2 == 0:
#             total = total+num
#     return total
# print(sum_of_even(10))
# def even_odd(number):
#     count = 0
#     for num in range(0,number+1):
#         if num%2==1:
#             count=count+1
#     print('the number of odd is ',count )
        
#     return count
# print(even_odd(100))
# def even_odd(number):
#     count = 0
#     for num in range(0,number+1):
#         if num%2==0:
#             count=count+1
            
#     print('the number of even is ',count )
        
#     return count
# print(even_odd(100))
# def fact(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact*i
#     return fact
    
# print(fact(5))


    
