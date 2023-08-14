import sys

n, k = map(int, sys.stdin.readline().split())
n = int(n)
k = int(k)

# 참가 학생 수 / 한 방에 배정할 수 있는 최대인원 수
list = [0, 0, 0, 0, 0]
result = 0

for i in range(n):
    Sex, Year = map(int, sys.stdin.readline().split())
    Sex = int(Sex)
    Year = int(Year)

    if Year == 3 or Year == 4:
        if Sex == 0:
            list[0] += 1
        else:
            list[1] += 1
    elif Year == 5 or Year == 6:
        if Sex == 0:
            list[2] += 1
        else:
            list[3] += 1
    else:
        # 1, 2학년
        list[4] += 1

# -1의 나머지를 구하면 오류가 남. 예외처리 필요.
for i in list:
    if i != 0:
        result += ((i - 1) // k + 1)
print(result)
