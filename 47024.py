'''Дана последовательность натуральных чисел.
Необходимо определить количество её непрерывных подпоследовательностей, сумма элементов которых кратна 1111.'''

with open("47024") as f:
    n = int(f.readline())
    nums = [
        int(line) for line in f
    ]

maxsum = 0
maxlen = 0 #количество подпоследовательностей
for begin in range(len(nums)):
    for end in range(begin, len(nums)):
        s = sum(nums[begin:end +1])
        if s % 1111 == 0:
            maxlen += 1

print(maxlen)

