# Formatting of Strings using format() method
string1 = input("Enter the string: ")
# Split the string into words
w1, w2, w3 = string1.split()
# Default order
print("Print String in default order:")
print("{} {} {}".format(w1, w2, w3))
# Positional order
print("\nPrint String in Positional order:")
print("{1} {0} {2}".format(w1, w2, w3))
# Keyword order
print("\nPrint String in order of Keywords:")
print("{c} {b} {a}".format(a=w1, b=w2, c=w3))