n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    
    log = 0
    for i in tree:
        if i > mid:
            log += i - mid
        
    if log >= m: #end를 줄이면 mid가 작게 잡혀 잘리는 log가 많아짐.
        start = mid + 1
    else:
        end = mid - 1

print(end)

