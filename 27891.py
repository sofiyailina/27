'''
Последовательность натуральных чисел характеризуется числом x— наибольшим числом, кратным 14 и
являющимся произведением двух элементов последовательности с различными номерами.
Гарантируется, что хотя бы одно такое произведение в последовательности есть.
'''
'''with open("27-A_27891.txt") as f:
    nums = [int(line) for line in f]

count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        a, b = int(nums[i]), int(nums[j])
        if a * b % 14 == 0:
            print(a*b)
'''
x = [8960, 156352, 383040, 347200, 68096, 405888, 239232, 3584, 443968, 350784, 300608, 436352, 36992, 408128, 174272, 146944, 141568, 123200, 33600, 447552]
print(max(x))
