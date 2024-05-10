# 1. Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as: (4/3)*Pi*r^3
import math
def vol(rad):
	return (4/3)*math.pi*math.pow(rad, 3)
# # Check
# print(f'1. Volume of a sphere is {vol(2)}')
# 33.49333333333333

# 2. Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
	if num in range(low, high+1):
		return f'{num} is in the range between {low} and {high}'
	else: return f'{num} is NOT in the range between {low} and {high}'
# # Check
result1 = ran_check(5,2,7)
# print(result1)
# 5 is in the range between 2 and 7
# If you only wanted to return a boolean:
def ran_bool(num,low,high):
	return num in range(low, high+1)
result2 = ran_bool(3,1,10)
# print(result2)
# True

# 3. Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!
import re
def up_low(s):
	up = 0
	low = 0
	# new_s = re.sub(r'[^\w\s]', '', s).split()
	# for word in new_s:
	# 	for letter in word:
	# 		if letter.isupper():
	# 			up += 1
	# 		else: low += 1
	# return up, low
	for char in s:
		if char.isupper():
			up +=1
		elif char.islower():
			low +=1
		else: pass
	return up, low

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
letters = up_low(s)
print(f'up and low: {letters}')
# Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters :  4
# No. of Lower case Characters :  33

# 4. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    return set(list(lst))
new_list = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
# [1, 2, 3, 4, 5]

# 5. Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
def multiply(numbers):
	result = 1
	for num in numbers:
		result = result*num
	return result
new_list = multiply([1,2,3,-4])
# -24

# 6. Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
def palindrome(s):
	new_s = s.replace(' ', '')
	return new_s == new_s[::-1]
palindrome('helleh')
# True


# Hard:
# 7. Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: You may want to use .replace() method to get rid of spaces.
# Hint: Look at the string module
# Hint: In case you want to use set comparisons
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
	# new_str = str1.replace(' ', '').lower()
	# letters = ''.join(sorted(set(new_str)))
	# return letters == alphabet
 alphaset = set(alphabet)
 str1 = str1.replace(' ', '').lower()
 str1 = set(str1)
 return str1 == alphaset
print(ispangram("The quick brown fox jumps over the lazy dog"))
# True
# string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
