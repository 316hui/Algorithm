t = int(input())
stac = []

for i in range(t):
    flag = None
    stac = []

    s = input()

    for j in range(len(s)):
        if s[j] == '(':
            stac.append('(')
        elif s[j] == ')':
            if len(stac) == 0:
                flag = False
                break
            stac.pop() #제일 뒤 삭제


    if len(stac) != 0 or flag == False:
        print("NO")
    else:
        print("YES")
