for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz') 
        # the fact that i have to do number 15 first is because 15 is divisible by both 3 and 5
        # so if I check for 3 or 5 first, it will never reach this condition
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else :
        print(i)