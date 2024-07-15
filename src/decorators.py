# def func():
# 	return 1

# def hello():
# 	return 'Hello!'

# #greet now is pointing to hello. If we delete hello, greet will still have pointer to the object
# greet = hello

# def newHello(name='Kitty'):
# 	print('The hello() function has been executed')
# 	def greet():
# 		return '\t This is greet() function inside hello'
# 	def welcome():
# 		return '\t This is welcome() inside hello'
# 	# print(greet())
# 	# print(welcome())
# 	if name == 'Kitty':
# 		return greet
# 	else:
# 		return welcome

# new_func = newHello('Mat')
# print(new_func())


# def new_decorator(original_func):
# 	def wrap_func():
# 		print('Code before original func')
# 		original_func()
# 		print('Code after original func')
# 	return wrap_func

# def need_decorator():
# 	print('I need to be decorated')

# decorated_func = new_decorator(need_decorator)
# decorated_func()

# @new_decorator
# def need_decorator():
# 	print('I need to be decorated')

# need_decorator()

# ----------------------GENERATORS:----------------------------
# takes less memory
def create_cubes(n):
	for x in range(n):
		yield x**3

for x in create_cubes(10):
	print(x)

def gen_fibon(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		a,b = b, a+b #reassigning a to b and b to a+b

for num in gen_fibon(10):
	print(num)
