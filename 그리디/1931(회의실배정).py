import sys

N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int,sys.stdin.readline().split())))
time.sort(key = lambda x:(x[1],x[0]))

cnt = 0
now = 0
for i in range(N):
    if now<=time[i][0]:
        now = time[i][1]
        cnt+=1
print(cnt)