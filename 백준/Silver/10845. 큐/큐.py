import sys

n = int(input())
Q = []

for i in range(n):
    inputt = sys.stdin.readline().split()

    if len(inputt) == 2:
        if inputt[0] == "push":
            Q.append(inputt[1])
    else:
        a = inputt[0]

        if a == "pop":
            if len(Q) != 0:
                print(Q[0])
                del Q[0]
            else:
                print(-1)
        if a == "size":
            print(len(Q))
        if a == "empty":
            if len(Q) == 0:
                print(1)
            else:
                print(0)
        if a == "front":
            if len(Q) != 0:
                print(Q[0])
            else:
                print(-1)
        if a == "back":
            if len(Q) != 0:
                print(Q[-1])
            else:
                print(-1)
