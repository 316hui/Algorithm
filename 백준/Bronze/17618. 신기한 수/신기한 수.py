import sys

n = int(sys.stdin.readline())
cntt = 0

for i in range(1, n + 1):
    result = 0
    num = i
    while num != 0:
        result += num % 10
        num //= 10
    
    if i % result == 0:
        cntt += 1

print(cntt)