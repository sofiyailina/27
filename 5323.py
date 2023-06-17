'''На вход программе поступает последовательность натуральных чисел.
Найдите непрерывную подпоследовательность с максимальной суммой,
в которой сумма элементов на четных позициях равна сумме элементов на нечетных позициях.'''
f = open('5323')
n = int(f.readline())
data = []
for line in f:
    k = int(line)
    data.append(k)

maxsum = 0
for begin in range(len(data)):
    for end in range(len(data)):
        seq = data[begin:end+1]
        четнаясумма = нечетнаясумма = 0
        for i in range(len(seq)):
            if i % 2 == 0:
                четнаясумма += seq[i]
            else:
                нечетнаясумма += seq[i]
        if четнаясумма == нечетнаясумма:
            sum = четнаясумма + нечетнаясумма
            if sum > maxsum:
                maxsum = sum
print(maxsum)