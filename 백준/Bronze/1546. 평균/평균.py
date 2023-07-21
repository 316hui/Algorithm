summ = 0
n = int(input())
s = list(map(int, input().split()))
maximum = max(s)

new_list = []
for i in s:
    new_list.append(i/maximum * 100)

print(sum(new_list)/n)
