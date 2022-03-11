import sys
from collections import deque
N,L,R = map(int,sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    global flag
    q = deque()
    q.append((i,j))
    visit[i][j] = 0
    cnt=1
    sum = ground[i][j]
    check = [[-1]*N for _ in range(N)]
    check[i][j] = 0
    while q:
        x,y = q.popleft()
        temp = ground[x][y]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == -1:
                if L<=abs(ground[nx][ny]-temp)<=R:
                    q.append((nx,ny))
                    visit[nx][ny] = 0
                    check[nx][ny] = 0
                    cnt+=1
                    sum+=ground[nx][ny]
    people = sum//cnt
    if cnt!=1:
        for i in range(N):
            for j in range(N):
                if check[i][j] == 0:
                    ground[i][j] = people
        flag= True
answer = 0     
while(1):
    flag = False
    visit = [[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1:
                bfs(i,j)
    if flag== False:
        break
    answer+=1
print(answer)