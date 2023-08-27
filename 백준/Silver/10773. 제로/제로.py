import sys

k = int(sys.stdin.readline())
writeList = []
cntt = 0

for i in range(k):
    n = int(input())

    if n == 0 and len(writeList) != 0:
        del writeList[-1]
    else:
        writeList.append(n)

print(sum(writeList))
