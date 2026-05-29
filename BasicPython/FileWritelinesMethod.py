myobject=open("myfile.txt",'w')
lines=["Hello everyone\n","Writing #multiline strings\n","This id the #third line"]
print(myobject.writelines(lines))
myobject.close()
