with open("27-A(5840).txt") as f:
    N, M = map(int, f.readline().split())
    nums = [int(line) for line in f]

def distance(i, j):
    d = abs(i - j)
    if d > N // 2:
        d = N - d
    return d * 3

def calc(i):
    s = 0
    for j in range(len(nums)):
        if j == i:
            continue
        d = distance(i, j)
        if d >= M:
            s += nums[j]
    return s

maxS = 0
maxI = -1
for i in range(len(nums)):
    s = calc(i)
    if s > maxS:
        maxS = s
        maxI = i
print(maxI * 3)