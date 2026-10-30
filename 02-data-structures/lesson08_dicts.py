person = {'name': 'Ayet', 'age': 22}

person['city'] = 'Melaka'   # adding a new key-value pair to the dictionary
print(person['name'])       # look up a value by key
print(person.get('job', 'none')) # safe look up with a default value if the key doesn't exist

for key, value in person.items():  # iterate over key-value pairs
    print(key, value)

# count letters
counts = {}
for ch in 'banana':
    counts[ch] = counts.get(ch, 0) + 1
print(counts)   # {'b': 1, 'a': 3, 'n': 2

print('a' in counts) # True, instant check if a key exists in the dictionary}