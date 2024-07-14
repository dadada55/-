n = int(input())
info = []
for i in range(n):
    a, b = map(int,input().split())
    info.append((a,b))
info.sort(reverse=True)

cnt = 0
largest = 0
for i in range(n):
    if largest < info[i][1]:
        largest = info[i][1]
        cnt += 1
print(cnt)