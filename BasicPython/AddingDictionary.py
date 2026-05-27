#adding
thisdict={'brand':'Ford','model':'Mustang','year':1964}
thisdict['color']='red'
print(thisdict)
#traversal
for x in thisdict:
    print(x,thisdict[x])


################################
#Update
d={1:'one',2:'two'} 
d1={3:'three'}
d.update(d1)
print(d)

#################################
#Comprehension
squares={x:x*x for x in range(5)}
print(squares)
