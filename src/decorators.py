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


def new_decorator(original_func):
	def wrap_func():
		print('Code before original func')
		original_func()
		print('Code after original func')
	return wrap_func

# def need_decorator():
# 	print('I need to be decorated')

# decorated_func = new_decorator(need_decorator)
# decorated_func()

@new_decorator
def need_decorator():
	print('I need to be decorated')

need_decorator()
