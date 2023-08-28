n = int(input())
inputn = list(map(int, input().split()))
m = int(input())
inputm = list(map(int, input().split()))
inputn.sort()

for i in inputm:
    target = i

    left = 0
    right = len(inputn)-1

    result = 0
    while left <= right:
        mid = (left + right) // 2
        if inputn[mid] == target:
            #답이 맞게 된 경우.
            result = 1
            break
        elif inputn[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    print(result)
