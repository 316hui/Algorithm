import sys

def getnum(a, b):
    x = max(a, b)
    y = min(a, b)
    while True:
        temp = x % y
        if temp == 0:
            result = y
            break
        x = y
        y = temp
    return result * (a//result) * (b//result)

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, input().split())
    print(getnum(a, b))