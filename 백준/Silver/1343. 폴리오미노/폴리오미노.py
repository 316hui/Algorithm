s = input()

s = s.replace("XXXX", "AAAA") #대체 함
s = s.replace("XX", "BB")

if "X" in s:
    print(-1)
else:
    print(s)

