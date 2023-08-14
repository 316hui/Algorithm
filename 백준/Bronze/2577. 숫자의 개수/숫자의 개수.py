import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

multi = a * b * c
multi = str(multi)

list = [0 for i in range(10)]

for i in multi:
        list[int(i)] += 1

for i in list:
    print(i)

