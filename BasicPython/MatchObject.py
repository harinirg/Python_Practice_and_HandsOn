import re
text='''Alan aturingb was a pioneer of aturingb computer and artificial inteligence.He was born on 23 June 1912 in Maida Vale,London'''
res=re.search("computer",text)
print("Match Object={}",format(res))
print("-"*30)
print("Group method output=",res.group())
print("-"*30)
print("Group method output=",res.start())
print("-"*30)
print("Group method output=",res.end())
print("-"*30)
print("Group method output=",res.span())
print("-"*30)
print("Group method output=",res.re)
print("-"*30)
print("Group method output=",res.string)
print("-"*30)
import re
pattern = r'\b\w+ing\b'
word = "Walking and talking are important activities"
match_result = re.findall(pattern, word)
if match_result:
    print("Match found: ",match_result)
else:
    print("No match found")
email_Pattern=r'\b[A-za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text_with_emails="Contact us at trainer@smartcliff.in or gayathri.monoj@smartcliff.in"
email_found=re.findall(email_Pattern,text_with_emails)
if email_found:
    print("Email addresses found:",email_found)
else:
    print("No mail addresses found")

