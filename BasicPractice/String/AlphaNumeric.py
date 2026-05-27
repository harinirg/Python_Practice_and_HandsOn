Input=input("Enter the sentence: ")
words=Input.split()
for word in words:
    if word.isalnum():
        for ch in word:
            if ch.isdigit():
                print(word)
                break