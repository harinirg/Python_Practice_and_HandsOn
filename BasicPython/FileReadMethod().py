myobject=open("myfile.txt",'r')
var=myobject.read(10)
print(var)
myobject.close()
###########################
#readline()
myobject=open("myfile.txt",'r')
print(myobject.readline())
print(myobject.readline())
print(myobject.readline())
################################
#readlines()
myobject=open("myfile.txt",'r')
print(myobject.readlines())
myobject.close()
#################################
#readlines()
myobject=open("myfile.txt",'r')
d=myobject.readlines()
for line in d:
    words=line.split()
    print(words)
#################################
#splitines()
myobject=open("myfile.txt",'r')
d=myobject.readlines()
for line in d:
    words=line.splitlines()
    print(words)
###################################
print("Now reading the contents of file")
fobject=open("myfile.txt",'r')
d=fobject.readlines()
for str in d:
    print(str)
fobject.close()

