with open('5789A.txt') as f:
    N, M = map(int, f.readline().split())
    data = [
        list(map(int, line.split()))
        for line in f
    ]
