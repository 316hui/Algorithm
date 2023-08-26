n = int(input())

for i in range(n):
    num = input()
    reverseNum = num[::-1]

    sum = int(num) + int(reverseNum)

    if str(sum) == (str(sum)[::-1]):
        print("YES")
    else:
        print("NO")
