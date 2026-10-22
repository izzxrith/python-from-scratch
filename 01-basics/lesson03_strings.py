word = 'Hello World'

print(len(word))  # 11, how many characters are in the string
print(word.upper()) # HELLO WORLD - it converts the string to uppercase
print(word.lower()) # hello world - it converts the string to lowercase
print(word[0]) # H, first letter is number 0
print(word[-1]) # d, last letter is number -1
print(word[0:5]) # Hello, letters 0 up to (not including) 5
print(word.split(' ')) # ['Hello', 'World'], splits the string into a list of words
print(word.replace('World', 'Ayet')) # Hello Ayet, replaces 'World' with 'Ayet'

name = 'Ayet'
print(f"Hi {name}, you are {2026 - 2004} years old.") # Hi Ayet, you are 22 years old. - f-string formatting