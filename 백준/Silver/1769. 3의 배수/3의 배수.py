n = input()
cnt = 0

while len(n) > 1:
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    n = str(sum)
    cnt += 1
print(cnt)
if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")