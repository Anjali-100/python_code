
# def year_is_leap(year):
#     if year % 4 == 0:
#         print(f"{year} is leap year.")
#     else:
#         print(f"{year} is not leap year.")
# year_is_leap(year = int(input("Input year: ")))
# n = int(input("Enter a size: "))
# for i  in range(1, n+1):
#     print( i * "*", end =" " )
#     # print(sep ="")
# n = int(input("Enter a size: "))
# fact = 1
# sum = 0
# for i in range(1,n+1):
#     fact = fact*i
#     ans = 1 / fact 
#     sum += ans
# print(sum)
# n = int(input("Enter a size: "))

# sum = 0
# a = 0
# b = 1
# print(sum)
# for i in range(n+1):
    
#     sum = a+b 
#     a = b
#     b = sum
#     print(sum)
# s= input("input string ")
# def isPalindrome(s):
#     return s == s[::-1]
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")
# a =19
# b = 18
# c = 17
# if a>b and b>c:
#     print("a is greater")
# elif a<b and b<c:
#     print("c is greater")
# elif c>a and c<b:
#     print("b is greater")

# def print_factors(x):
#    print("The factors of",x,"are:")
#    for i in range(1, x + 1):
#        if x % i == 0:
#            print(i)
# print_factors(x = int(input("enter a number ")))

# for i in range(0,101):
#     f = (i*9/5)+32
#     print(f"{i} Celcius  {f} Farenhite") 
# for x in range(0,10,0.2):
#     print(tan(x))
import math

x = 0.0

# while x <= 10.0:
#     sin_value = math.sin(x)
#     cos_value = math.cos(x)
#     tan_value = math.tan(x)
    
#     print(f"x = {x:.1f}: sin(x) = {sin_value:.4f}, cos(x) = {cos_value:.4f}, tan(x) = {tan_value:.4f}")
    
#     x += 0.2
def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the method
num1 = 36
num2 = 48
gcd = calculate_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")





