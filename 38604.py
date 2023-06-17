'''Дана последовательность из N натуральных чисел.
Рассматриваются все её непрерывные подпоследовательности, такие что сумма элементов каждой из них кратна k=43.
Найдите среди них подпоследовательность с максимальной суммой, определите её длину.
Если таких подпоследовательностей найдено несколько, в ответе укажите количество элементов самой короткой из них.'''
with open("38604") as f:
    n = int(f.readline())
    nums = [
        int(line) for line in f
    ]

maxsum = 0
maxlen = 0
for begin in range(len(nums)):
    for end in range(begin, len(nums)):
        s = sum(nums[begin:end + 1])
        if s % 43 == 0:
            l = end - begin +1
            if s > maxsum:
                maxsum = s
                maxlen = l
            elif s == maxsum:
                if l < maxlen:
                    maxlen = l

print(maxlen)