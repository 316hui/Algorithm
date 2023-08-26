n = int(input())

for i in range(n):
    num = int(input())
    lenN = len(str(num))

    if str(num**2)[-lenN:] == str(num):
        print("YES")
    else:
        print("NO")

