def is_even(n):
    return n % 2 == 0

def reverse_string(s):
    result = ''

    for ch in s:
        result = ch + result
    return result

def count_vowels(s):
    total = 0
    for ch in s.lower():
        if ch in 'aeiou':
            total += 1
        return total

if __name__ == '__main__':
    print(is_even(4)) # True
    print(reverse_string('ayet')) # teya
    print(count_vowels('Hello World')) # 3