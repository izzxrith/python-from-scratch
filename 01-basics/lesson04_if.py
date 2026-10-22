n = 7

if n % 2 == 0: # 7/2 = 3 remainder 1, so 7 is odd
    print("n is even")
else:
    print("n is odd")

score = 65
if score >= 80: # 65 is not >= 80
    print('A')
elif score >= 50: # 65 is >= 50
    print('Pass')
else:
    print('Fail') # 65 is not >= 50 and not >= 80

age = 22
has_ticket = True
if age >= 18 and has_ticket:
    print('You can enter') # 22 >= 18 and has_ticket is True