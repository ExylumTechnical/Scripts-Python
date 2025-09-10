
for i in range(0,20,2):
	print(i)

# the range function is a generator

class Fib:
# accepts 1 number as an option upon initialization
# prints out __init__ on initialization
	def __init__(self, nn):
		print("__init__");
		self.__n = nn;
		self.__i = 0;
		self.__p1 = self.__p2 = 2

# __iter__ takes itself as the only input and outputs
# itself so that next may handle internal variubles
# the internal variubles are saved through the __iter__
# function and are passed to the __next__ function
# for processing
	def __iter__(self):
		print("__iter__");
		return self;

# __next__ defines what should be done with the internal
# variubles on each iteration
	def __next__(self):
		print("__next__");
		self.__i += 1;
		if self.__i > self.__n:
			raise StopIteration
# StopIteration will end the iteration of the __next__ definition
		if self.__i in [1,2]:
			return 1;
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

# the Fib class is initialized as part of the loop
for i in Fib(10):
	print(i)

# another way to call the generator inside of a different class

class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("class iter")
		return self.__iter

object = Class(8)
for i in object:
	print(i)


class foreverLoop:
	def __init__(self, x):
		self.__x = x
		self.__i = 0;

	def __iter__(self):
		return self

	def __next__(self):
		ret = self.__i + 1;
		self.__x, self.__i = self.__x, ret 
		return ret
#for i in foreverLoop(1):
#	print(i);


# Exact same result as a range function
# the yield will pause the state of the code then
# execute it again within a for loop
def loop(x):
	for i in range(x):
		yield i
print("Counting loop")
for v in loop(5):
	print(v)

def powersOf2(n):
	po = 1;
	for i in range(n):
		yield po;
		po *=2

print("powers of 2")
for v in powersOf2(4):
	print(v)


# something about list generation
lst = [1 if x % 2 == 0 else 0 for x in range(100)]
gen = (1 if x % 2 == 0 else 0 for x in range(20))

#print(lst)
#print(gen)

for x in lst:
	print(" ",x, end =" ")

for x in gen:
	print(" ",x, end =" ")


# lambdas are used to simplify code

add = lambda x, y: x + y
mult = lambda x, y: x*y
exp = lambda x, y: x**y

print(add(2,2))
print(mult(10,2))
print(exp(10,2))

# using the map function

# make a list
l1 = [x for x in range(5)]
# map takes the lambda as the first argument
# the elements from l1 are applied to the lambda as the argument
l2 = list(map(lambda x: 2**x, l1))
# l2 has a result of all elements being to the 2nd power
print(l2)
# Print the list passed through the lambda function a second time
for x in map(lambda x: x*x, l2):
	print(x,end=' ')
print()


# Using the filter function
from random import seed, randint
seed()
# create a datalist of 5 random ints from -10 to 10
data = [randint(-10,10) for x in range(5)]
# filter the list to be only positive even numbers
filtered = list(filter(lambda x: x > 0 and x%2 ==0, data))
print(data)
print(filtered)


# working with closures
def outer(par):
	# This funciton is a private tool used by the outer() function
	def inner_location():
		return loc
	loc = par;
	return inner_location

var = 1
loc = outer(var)
print(var)
print("Mem location : ",loc)
print(loc())

# the loc() declearation executes the function and passes arguments
# to the next layer of the function

def makeclosure(par):
	loc = par
	def power(p):
		return p** loc
	return power

fsqr = makeclosure(2)
fcub = makeclosure(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))
























