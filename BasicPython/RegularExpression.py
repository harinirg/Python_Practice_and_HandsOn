#Search
import re
text='''Alan aturingb was a pioneer of aturingb computer and artificial inteligence.He was born on 23 June 1912 in Maida Vale,London'''
res=re.search("^Alan.*London$",text)
if(res):
    print("We have a match")
else:
    print("We dont have a match")
#Findall
res1=re.findall('turing',text)
print("Result={}".format(res1))
#re.span
print("Result={}and start,end position={}".format(res,res.span()))
#Split
res2=re.split("a",text)
print("Result={}",format(res2))
#sub(Replace)
res3=re.sub("aturingb",'Turning',text)
print("Result={}".format(res3))


