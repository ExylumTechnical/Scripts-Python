# open a file and read each line with a with() statement
with open("file") as my_file:
    print(my_file.read())

# open a file and create it with the w mode
try:
	stream = open("file","rt")
	stream.close();
except IOError as exc:
	print("File not found :",exc.errno)
except:
	print("Unknown error")

# errno library will help determine what excactly caused
# a stream error
import errno
try:
	open("file","w")
except Exception as exc:
	print("Permission denied : ",exc)

stream = open("files/tzop.txt","rt", encoding="utf-8")
print(stream.read())

stream.close()
from os import strerror


try:
	s = open("files/tzop.txt","rt", encoding="utf-8")
	cnt = 0;
	ch = s.read(1)
	# read one charicter of the file
	while ch != '':
		print(ch,end='')
		cnt +=1
		ch = s.read(1)
	s.close()
	print("\n\nCharicters in the file: ",cnt)
	print("\n\n")
	s.close()
# the IOError will catch just about any file error that can occur
except IOError as e:
	# strerror will convert an error imported into a string
	# this is handy if implementation of the errno is entered
	# into the function as an argument.
	print("I/O error occured: ",strerror(e.errno))

try:
	s = open("files/tzop.txt","rt", encoding="utf-8")
	cnt = 0;
	ch = s.readline()
	cha = s.readlines(1); # prints python string parsable text
	print(cha)
except IOError as e:
	print("I/O error occured: ",strerror(e.errno))


# read charicters from a file
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

# read entire lines from a file
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))

# write to a file
from os import strerror

try:
	fo = open('newtext.txt', 'wt') # a new file (newtext.txt) is created
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
	print("Action completed")
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))

from os import system
system("cat newtext.txt")


# understanding bytearrays to understand binary files
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i
print(data)
for b in data:
    print(hex(b))

# Writing to a file from binary

# create a binary array
data = bytearray(10)
for i in range(len(data)):
	data[i] = 10 + i
# write the binary data into a file
try:
	bf = open('files/file.bin',"wb")
	bf.write(data)
	bf.close()
except IOError as e:
	print("I/O Error occured : ",strerr(e.errno))

try:
	bf = open('files/file.bin',"rb")
	a = bf.read(5); # supplying an integer to a read operation will request that only
			# that number of bytes be read from the file
	print(a);
except IOError as e:
	print("I/O Error occured : ",e)

try:
#	f = open('files/file',"rb")
	for i in open('files/tzop.txt',"rb"):
		print(i)
except IOError as e:
	print("I/O Error occured : ",e)

# using system streams
##import sys
# standard in typically the keyboard
##stin = sys.stdin
# standard out typically the terminal
##stout = sys.stdout
# standard error again usually the terminal but it is the output
# type that is associated with errors
##sterr = sys.stderr



#f = open("File",mode="w",buffering=-1,encoding=None,errors=None,closefd=True,opener=None);
# the above is the full definition of a file function to open a file
#f.write("Something new"); # this writes something to the file
#f.close(); # this closes the file so that it may be opened again
#aw = open("somefi","w"); # opened a new file again for writing
#aw.write(str(input("Enter some data "))) # input a string into the file;
#aw.close(); # there the file is closed
#ar = open("somefi","r") # opened the file again for reading this time
#print(ar.read(1)); # reading one charicter into the file
#print(ar.read(1)); # again only one charicter is read from the file
#print(ar.read()); # will this read the whole file? I think so
#ar.close(); # file is closed again for the final time...
#o.system("rm File") # oh no it has been deleted but that is okay
#o.system("rm somefi") # and the second follows it into the unkown.....
