def linux_path(file_name):
#	try:
	ct = len(file_name)
	fi = ''
	fi_pos = 0
	fi_ss = 0
	fi_se = ct
	while(len(file_name)+1 > len(fi)):
		fi_se = file_name.find(" ",fi_ss)
		fi = fi + file_name[fi_ss:fi_se]+" "
		fi_ss = fi_se +1
	return fi[:-2]

#	except TypeError:
#		print("Unsupported string passed as filename")
#	except:
#		print('Unknown Error occured durring parsing of filename')


from os import system, path
system("pwd > wd")
wd = open("wd","r")
z = wd.readline()
z = z[:-1]
z = linux_path(z)
finam = "somefi"
pa = z + '/'+finam

if(path.exists(pa)):
	x = open(pa,"w");
	x.write("Write successful")
else:
	y = input("Buffer file exists, do you want to overwrite?\n[Y/n]")
	if(y == "Y"):
		print("overwriting file");
		x = open(pa,"w");
		x.write("Write successful")
	else:
		print("Skipping file")
