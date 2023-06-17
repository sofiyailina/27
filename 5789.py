with open('5789A.txt') as f:
    N, M = map(int, f.readline().split())
    data = [
        list(map(int, line.split()))
        for line in f
    ]

def calc(i):
    рейсы = 0
    отправления = 0
    for j in range(N):
        расстояние = abs(data[i][0] - data[j][0])
        if расстояние <= M:
            отправления += data[j][1]
            рейсы += data[j][1] // 50
            if data [j][1] % 50 != 0:
                рейсы += 1
    return (отправления, рейсы)

макс_отпр = 0
мин_рейс = 1_000_000_000
for i in range(N):
    отправления, рейсы = calc(i)
    if отправления > макс_отпр:
        макс_отпр = отправления
        мин_рейс = рейсы
    elif отправления == макс_отпр and рейсы < мин_рейс:
        мин_рейс = рейсы

print(мин_рейс)