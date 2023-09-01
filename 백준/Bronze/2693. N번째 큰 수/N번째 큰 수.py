t = int(input())

for i in range(t):
    s = list(map(int, input().split()))
    s.sort()
    print(s[-3])
