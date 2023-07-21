n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
candiate = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candiate: #수가 있는지 없는지
    result = count.get(target) #그 수를 count 리스트에서 가져옴
    if result == None: #만약 아무내용 없으면 0
        print(0, end=" ")
    else: #있으면 (1~..) 리스트에서 해당 값 출력
        print(result, end=" ")