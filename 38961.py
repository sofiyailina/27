'''Дана последовательность натуральных чисел.
Необходимо найти максимально возможную сумму её непрерывной подпоследовательности, в которой количество чётных элементов кратно k = 10.'''

with open("38961") as f:
    n = int(f.readline())
    nums = [
        int(line) for line in f
    ]

maxsum = 0
maxlen = 0 #четные элементы
for begin in range(len(nums)):
    for end in range(begin, len(nums)):
        s = sum(nums[begin:end + 1])
        if s % 2 == 0 and s % 10 == 0:
            maxlen += 1

print(maxlen)
