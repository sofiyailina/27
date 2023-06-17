#статград 25102022
with open("27-A.txt") as f:
    nums = [int(line) for line in f]

count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        a, b = nums[i], nums[j]
        if (a + b) % 3 == 0 and (a * b) % 1024 == 0:
            count += 1

print(count)