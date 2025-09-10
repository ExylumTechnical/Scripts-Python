ten=[] # empty list created
z=1; # make z == to 1
# function to add z which is counted up to the end of the list
# ten.
for z in range(10):
	ten.append(z)
print(ten);

ten= [] # clear the list
print("\nNow reversed")
for z in range(10):
	ten.insert(0,z)
print(ten);

ten= []
e=0;
print("\nten odd numbers")
for z in range(10):
	e += 2;
	ten.append(e)
print(ten);

ten= []
e = 1;
print("\nten even numbers")
for z in range(10):
	e +=2;
	ten.append(e)
print(ten);

# print the total of all numberes in the list
num = [1,15,23,7,5]
e =0
for i in range(len(num)):
	e += num[i];
print("The sum of the list is", e)




l =[14,2,10,8,6,4,20,50,60,22,36,24,5,7]

print(l)
l.sort()
print(l)
print("List sorting")
l =[14,2,10,8,6,4,20,50,60,22,36,24,5]
print("The list is : ", l);

q = 0;


while(q <= len(l)):
	for i in range(len(l)-1):
		if(l[i] > l[i+1] ):
			l.append(l[i]);
			del(l[i])
		else: 
			i = i
	q += 1;


print("Sorted from lowest to highest",l)
q = 0;
while(q <= len(l)):
	for i in range(len(l)-1):
		if(l[i] < l[i+1] ):
			l.append(l[i]);
			del(l[i])
		else: 
			i = i
	q += 1;

print("Sorted from highest to lowest",l)
l =[14,2,10,8,6,4,20,50,60,22,36,24,5]
# using built in functions
l.sort() # sorts from lowest to highest
print(l);
l.reverse() # reverses the list without performing any sorting
print(l);
l_l = l[0];

# streamline
for i in l[1:]:
	if i > l_l:
		l_l = i;

print("Largest number in the list is :", l_l)

# finding specific elements in a list

find = int(input("Find this numbers place :"));
found = False;
for i in range(len(l)):
 	found = find == l[i];
 	if found:
 		break

if found:
	print(find,"can be found at place",i,"in the list");
else:
	print("Could not find",find,"in list");
	
# removing duplicate numbers

l = [1,2,4,4,1,4,2,6,2,9]
l_s = [];
l.sort();
lHigh = l[len(l)-1];

for a in range(lHigh):
	if a in l:
		l_s.append(a);
	else:
		continue;
l_s.append(lHigh);




print("There are no duplicates left in the following list",l_s,l,sep="\n")

# Simple functions for complicated problems

# automatic sorting
ten.sort(); # sorts the list from least to most
print(ten);
ten.reverse();
print(ten);

# automatic finding
l = [1,3,7,8];
s = ["A","B","C","E"]

print("Is A in list s?		","A" in s);
print("Is not D in list s?	","D" not in s);
print("Is 1 in list l?		",1 in l);
print("Is not 2 in list l?	",2 not in l);

# strings can be sorted as well
l = ["A","C","D","a","b","B","AB","BA"]
l.sort()
print(l)










	
	
	
