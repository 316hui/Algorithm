n = int(input())
cntt = 0
result = n


while True:
    a = result // 10
    b = result % 10
    c = (a+b) % 10
    result = (b * 10) + c

    cntt += 1
    if result == n:
        break

print(cntt)