import sys
# get the arguments
n = len(sys.argv)
# get the total number of arguments
print("Total number arguments passed:", n)
# the zeroth list element is the name of the script
print("\nName of the script:", sys.argv[0])
# dump all the arguments passed to the script
print("\nArguments passed to the script:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")