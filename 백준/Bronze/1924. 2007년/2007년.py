day = 0
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ['SUN', "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x-1):
    day += days[i]
day += y
#day를 다 더해 7로 나누면 요일이 나옴

result = day % 7
print(month[result])