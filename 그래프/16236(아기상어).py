import sys
from collections import deque
N = int(input())
ground = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
size = 2
for i in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))
    for j in range(len(ground[i])):
        if ground[i][j] == 9:
            ground[i][j] = 0
            babyx = i
            babyy = j
eat = 0
time = 0
while(True):
    q=deque()
    q.append((babyx,babyy,0))
    temp = []
    visit = [[-1]*N for _ in range(N)]
    visit[babyx][babyy] = 0
    while q:
        x,y,cnt = q.popleft()
        if ground[x][y] !=0 and ground[x][y] < size:
            temp.append((x,y,cnt))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == -1:
                if ground[nx][ny] <=size:
                    q.append((nx,ny,cnt+1))
                    visit[nx][ny] = 0   
    temp.sort(key = lambda x:(x[2],x[0],x[1]))
    if(len(temp)==0):
        break
    else:
        time += temp[0][2]
        eat += 1
        x= temp[0][0]
        y=temp[0][1]
        ground[x][y] = 0
        babyx = x
        babyy = y
        if(eat==size):
            eat = 0
            size+=1
print(time)
