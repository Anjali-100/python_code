# import random
# import string

# def generate_user_id():
#     alphabet = string.ascii_letters + string.digits
#     user_id = ''.join(random.choice(alphabet) for i in range(6))
#     return user_id
# print(generate_user_id())
# import random
# import string

# def user_id_gen_by_user():
#     id_length = int(input("Enter the length of the user ID: "))
#     num_ids = int(input("Enter the number of user IDs to generate: "))
#     alphabet = string.ascii_letters + string.digits
    
#     user_ids = []
#     for i in range(num_ids):
#         user_id = ''.join(random.choice(alphabet)  for j in range(id_length))
#         user_ids.append(user_id)
#         print(user_ids)
    
#     return user_ids
# print(user_id_gen_by_user())
# import random

# def rgb_color_gen():
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     return (red, green, blue)
# print(rgb_color_gen())
# color = rgb_color_gen()
# print(color)
# for i in range(10):
#     color = rgb_color_gen()
#     print(color)
# import random

# def list_of_hexa_colors(num_colors):
#     colors = []
#     for i in range(num_colors):
#         color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
#         colors.append(color)
#     return colors
# print(list_of_hexa_colors(5))
# import random

# def list_of_rgb_colors(num_colors):
#     colors = []
#     for i in range(num_colors):
#         red = random.randint(0, 255)
#         green = random.randint(0, 255)
#         blue = random.randint(0, 255)
#         color = (red, green, blue)
#         colors.append(color)
#     return colors
# print(list_of_rgb_colors(5))
# def generate_colors(num_colors, color_type):
#     if color_type == 'hex':
#         return list_of_hexa_colors(num_colors)
#     elif color_type == 'rgb':
#         return list_of_rgb_colors(num_colors)
    
    
# print(generate_colors(3,'hex'))
# import random

# def shuffle_list(lst):
#     random.shuffle(lst)
#     return lst
# print(shuffle_list([1,3,2,4,5]))
# import random

# def seven_random_numbers():
#     numbers = random.sample(range(10), 7)
#     return numbers
# print(seven_random_numbers())
# import random

# import string
# def random_user_id():
#     alphabet = string.ascii_letters + string.digits
#     user_id = ''.join(random.choice(alphabet) for i in range (6))
#     return user_id

# print(random_user_id())    
# import random
# import string
# def user_id():
#     a = int(input('number of charecter '))
#     b = int(input("number of IDs "))
#     alphabet = string.ascii_letters + string.digits
#     user= []
#     for i in range(b):
#         users = ''.join(random.choice(alphabet) for j in range (a))
#         user.append(users)
#         print(users)
#     return users
# print(user_id())
import random
def rgb_color_gen():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r ,g ,b)
print(rgb_color_gen())
color = rgb_color_gen()
print(color)
# for i in range(10):
color = rgb_color_gen()
print(color)


