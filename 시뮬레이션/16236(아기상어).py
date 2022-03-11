import sys
from collections import deque
N = int(input())
ground = []
sx = 0
sy = 0
for i in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if ground[i][j]==9:
            sx = i
            sy = j
            ground[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,1,-1]
size = 2
time = 0
cnt = 0
def find():
    global time
    global size
    global sx,sy,cnt
    q = deque()
    q.append((sx,sy,0))
    visit = [[-1]*N for _ in range(N)]
    visit[sx][sy] = 0
    target = []
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == -1:
                if ground[nx][ny]==0:
                    visit[nx][ny] = 0
                    q.append((nx,ny,dist+1))
                else:
                    if ground[nx][ny] == size:
                        visit[nx][ny]=0
                        q.append((nx,ny,dist+1))
                    if ground[nx][ny]<size:
                        target.append((nx,ny,dist+1))
                        visit[nx][ny] = 0
    target.sort(key=lambda x:(x[2],x[0],x[1]))
    if len(target)==0:
        return False
    else:
        sx = target[0][0]
        sy = target[0][1]
        time += target[0][2]
        cnt+=1
        if cnt==size:
            size+=1
            cnt=0
        ground[sx][sy] = 0
        return True
while(1):
    check = find()
    if check==False:
        break
print(time)