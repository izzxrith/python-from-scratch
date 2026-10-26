nums = [3, 1, 4, 1, 5]

nums.append(9)          # add to the end
nums.remove(1)          # remove the first 1
print(nums[0])          # first box - starts with 0
print(len(nums))        # how many boxes
print(nums[1:3])        # slice - boxes 1 and 2
print(sorted(nums))     # sorted copy

total = 0
for n in nums:
    total += n
print('sum', total, 'max', max(nums), 'min', min(nums))

evens = [n for n in nums if n % 2 == 0]  # list comprehension
print(evens)

for index, value in enumerate(nums):
    print(index, value)