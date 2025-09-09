try:
	raise Exception
except BaseException:
	print("a")
except Exception:
	print("b")
except:
	print("c")

try:
	raise Exception(1,2,3)
except Exception as e:
	print(len(e.args))



def reciprocal(n):
	try:
		n = 1/n;
	except ZeroDivisionError:
		print("Division Failed due to number being zero");
	else:# executes only if try block is successful
		print("Division Successful")
		return n;
	finally:# execute no matter if try was successful or not
		print("Completion of try block")
		return n;




print(reciprocal(2));
print(reciprocal(0));

# Exceptions are classes

try:
	i = int("Hello!")
except Exception as e:
	print(e);
	print(e.__str__())

# print the entire exception tree
def printExcTree(thisclass, nest = 0):
	if nest >1:
		print("   |"*(nest-1),end="");
	if nest > 0:
		print("   +---",end="")
	print(thisclass.__name__);
	for subclass in thisclass.__subclasses__():
		printExcTree(subclass,nest+1)
printExcTree(BaseException)

# output is an example of a recursive data structure the definition includes
# to arguments
#	- a point inside the tree to start traversing
#	- a nesting level that is used to draw the trees branches


# more detailed anatomy of an exception

def printargs(args):
	lng = len(args);
	if(lng == 0):
		print("");
	elif(lng==1):
		print(args[0]);
	else:
		print(str(args))

try:
	raise Exception
except Exception as e:
	print(e, e.__str__(), sep=" : ", end=" : ");
	printargs(e.args)

# Rased exceptions can have custom exception strings defined when raised
try:
	raise Exception("my exception")
except Exception as e:
	print(e, e.__str__(), sep=" : ", end=" : ");
	printargs(e.args)

try:
	raise Exception("my","exception")
except Exception as e:
	print(e, e.__str__(), sep=" : ", end=" : ");
	printargs(e.args)


# creating a custom Exception
class MyZeroDivisionError(ZeroDivisionError):
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("some custom bad news");
	else:
		raise ZeroDivisionError("some bad news")

for mode in [False,True]:
	try:
		doTheDivision(mode)
	except BaseException:
		print('baseerror')
	except ZeroDivisionError:
		print('Division by zero')

for mode in [False,True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('My division by zero')
	except ZeroDivisionError:
		print('Original division by zero')

# When exceptions are raised in this example they do not need all previous
# options specified


# Definition of the pizza error
class PizzaError(Exception):
	def __init__(self, pizza='unkown', message=''):
		Exception.__init__(self,message)
		self.pizza = pizza;

# definition of cheese error
class TooMuchCheeseError(PizzaError):
	def __init__(self, pizza='unknown', cheese='>100', message=''):		
		PizzaError.__init__(self, pizza, message)
		self.cheese = cheese

def makePizza(pizza, cheese):
	if pizza not in ['margherita','capricciosa','calzone']:
		raise PizzaError
	if cheese > 100:
		raise TooMuchCheeseError
	else:
		print("Pizza Done")

for (pz, ch) in [('calzone',0),('margherita',110),('mafia',20)]:
	try:
		makePizza(pz,ch)
	except TooMuchCheeseError as tmce:
		print(tmce, ':', tmce.cheese)
	except PizzaError as pe:
		print(pe,':',pe.pizza)



