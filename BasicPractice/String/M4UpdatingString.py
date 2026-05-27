# Updating a Character in a String using Indexing
string1 = input("Initial String: ")
updated_string = string1[:2] + 'p' + string1[3:]
print("Updating character at 2nd Index:")
print(updated_string)