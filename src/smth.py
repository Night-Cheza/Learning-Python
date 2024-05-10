# from random import shuffle

# def say_hello(name):
# 	print(f'Hello {name}')

# say_hello('Sam')

# mylist = [20,5,3,90,1,45,36,102,53]

# def shuffle_list(list):
# 	shuffle(list)
# 	return list

# shuffled = shuffle_list(mylist)
# print(shuffled)

# mylist.sort()
# print(mylist)

# def string_func(string):
#     mystr = ''
#     for index, letter in enumerate(string):
#         if index == 0 or index%2 == 0:
#             letter = string[index].capitalize()
#         mystr +=letter
#     print(mystr)
#     return mystr

# string_func('asdfghjklpty')
# print(formatted)

# def square(num):
# 	return num**2
# my_nums = [1, 2, 3, 4, 5]
# for num in map(square, my_nums):
# 	print(num)
# mylist = list(map(square, my_nums))
# print(mylist)

# def even(names):
# 	if len(names)%2 == 0:
# 		return 'EVEN'
# 	else:
# 		return names[0]
# names = ['Helen', 'Andy', 'Sally']
# name = list(map(even, names))
# print(name)

# def check_even(num):
# 	return num%2 == 0
# my_nums = [1,2,3,4,5,6]
# even_list = list(filter(check_even, my_nums))
# print(even_list)

# nums = [11, 12, 13, 14, 15, 16]
# even_list = list(filter(lambda num: num%2 == 0, nums))
# print(even_list)

# first_letter = list(map(lambda name: name[0], names))
# print(first_letter)

# sentense = 'This is my sentense'
# print(' '.join(sentense.split()[::-1]))
# print(sentense[::-1])

# print('1'.isdigit())

class Cat():
	type = 'mammal'

	def __init__(self, name, color):
		self.name = name
		self.color = color

#here don't pass self.activity as it is not defining the object/class
	def says(self, activity):
		print(f'Mew! My name is {self.name} and I want to {activity}')

my_cat = Cat('Mirra', 'black')
print(my_cat.type)
my_cat.says('play')
