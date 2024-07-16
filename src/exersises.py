# 1.LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		return min(a,b)
	else:
		return max(a, b)
# # Check
lesser_of_two_evens(2,4)
# # Check
lesser_of_two_evens(2,5)

# 2. ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
	word1, word2 = text.split()
	if(word1[0] == word2[0]):
		return True
	else:
		return False

# # Check
animal_crackers('Levelheaded Llama')
# # Check
animal_crackers('Crazy Kangaroo')

# 3. MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
	if n1+n2 == 20 or n1 == 20 or n2 == 20:
		return True
	else:
		return False
# # Check
makes_twenty(20,10)
# # Check
makes_twenty(2,3)


# LEVEL 1 PROBLEMS
# 4. OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'
# Another solution:
# def old_macdonald(name):
# 	if len(name) > 3:
# 		return name[:3].capitalize() + name[3:].capitalize()
def old_macdonald(name):
	newname = ""
	for index, letter in enumerate(name):
		if index == 0 or index == 3:
			letter = name[index].capitalize()
		newname += letter
	return newname
# # Check
old_macdonald('macdonald')

# 5. MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
# >>> " ".join(['Hello','world'])
# >>> "Hello world"
def master_yoda(text):
	words = text.split()
	words.reverse()
	return ' '.join(words)
# # Check
master_yoda('I am home')
# # Check
master_yoda('We are ready')

# 6. ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number
def almost_there(n):
	if abs(n-100) <= 10 or abs(n-200) <= 10:
		return True
	else:
		return False
# # Check
almost_there(104)
# # Check
almost_there(150)
# # Check
almost_there(209)

# LEVEL 2 PROBLEMS
# 7. FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
# Another solution:
# def has_33(nums):
# 	for i in range(0, len(nums)-1):
# 		if nums[i] == 3 and nums[i+1] == 3:
# 			return True
# 	return False
def has_33(nums):
	index = 0
	while index < len(nums):
		if 3 in nums and nums[nums.index(3)+1] == 3:
			return True
		else:
			return False
# # Check
has_33([1, 3, 3])
# # Check
has_33([1, 3, 1, 3])
# # Check
has_33([3, 1, 3])

# 8. PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
	newtext = ''
	for letter in text:
		newtext += letter*3
	return newtext
# # Check
paper_doll('Hello')
# # Check
paper_doll('Mississippi')

# 9. BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(a,b,c):
	if sum((a,b,c)) <= 21:
		return sum((a,b,c))
	elif (sum((a,b,c)) <= 31) and 11 in (a,b,c):
		return sum((a,b,c)) - 10
	else: return 'BUST'
# # Check
blackjack(5,6,7)
# # Check
blackjack(9,9,9)
# # Check
blackjack(9,9,11)

# 10. SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(arr):
	for num, index in enumerate(arr):
		if len(arr) == 0:
			return
		while index < len(arr):
			if 6 and 9 in arr:
				return sum(arr[0:arr.index(6)]+arr[arr.index(9)+1:])
			else: return sum(arr)
# # Check
summer_69([1, 3, 5])
# # Check
summer_69([4, 5, 6, 7, 8, 9])
# # Check
summer_69([2, 1, 6, 9, 11])

# CHALLENGING PROBLEMS
# 11. SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
	spy = []
	for num in nums:
		if num == 0 or num == 7:
			spy.append(num)
	if spy == [0,0,7]:
		return True
	else: return False
# # Check
spy_game([1,2,4,0,0,7,5])
# # Check
spy_game([1,0,2,4,0,5,7])
# # Check
spy_game([1,7,2,0,4,5,0])

# 12. COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.
def count_primes(num):
	if num < 2:  # for the case of num = 0 or 1
		return 0
	primes = [2]
	x = 3 # starting with 3 so we can have step of 2 skipping even numbers
	while x <= num:
		for y in range(3,x,2):  # test all odd factors from 3 to x with step of 2
			if x%y == 0:
				x += 2
				break
		else:
				primes.append(x)
				x += 2
	print(primes)
	return len(primes)
# # Check
print(f'12. Return 25: {count_primes(100)}')

#----GENERATORS------

# Problem 1
# Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
	for num in range(N):
		yield num**2

for x in gensquares(10):
	print(x)

# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library.
import random

def rand_num(low,high,n):
	for x in range(n):
		yield random.randint(low, high)

for num in rand_num(1,10,12):
	print(num)

# Problem 3
# Use the iter() function to convert the string below into an iterator
s = 'hello'
new_s = iter(s)
print(next(new_s))
print(next(new_s))
