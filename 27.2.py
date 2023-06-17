'''
Дана последовательность натуральных чисел.
Назовём парой любые два числа из последовательности.
Необходимо определить количество пар, в которых сумма чисел в паре делится без остатка на 3, а их произведение – на 4096.
'''
with open('') as f:
    nums = [int(line) for line in f]

count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        a, b = nums[i], nums[j]
        if (a + b) % 3 == 0 and (a * b) % 4096 == 0:
            count += 1

print(count)