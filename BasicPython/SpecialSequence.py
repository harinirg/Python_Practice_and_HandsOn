import re
text='''Alan aturingb was a pioneer of aturingb computer and artificial inteligence.He was born on 23 June 1912 in Maida Vale,London'''
res=re.findall(r"\AAlan",text)
print("Result for \\A=",res)
print("-"*79)
res=re.findall(r"\bLon",text)
print("Result for \\b=",res)
print("-"*79)
res=re.findall(r'\d',text)
print("Result for \\d=",res)
print("-"*79)
res=re.findall(r'\D',text)
print("Result for \\D=",res)
print("-"*79)

res=re.findall(r'\w',text)
print("Result for \\w=",res)
print("-"*79)

res=re.findall(r'\W',text)
print("Result for \\W=",res)
print("-"*79)
res = re.findall(r'London\Z', text)
print(res)

