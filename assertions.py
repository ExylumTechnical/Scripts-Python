a = 10
assert a == 10
print(a)
a = 11
try:
	assert a == 10
except AssertionError:	
	print("Error : Assertion of a == 10 failed ")
print(a)
