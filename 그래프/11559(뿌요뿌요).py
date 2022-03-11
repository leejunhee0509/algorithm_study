import sys
from collections import deque
ground = []
for _ in range(12):
    ground.append(list(map(str,sys.stdin.readline().strip())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
check = False

def bomb(i,j):
    global check
    q= deque()
    q.append((i,j))
    visit = [[-1]*6 for _ in range(12)]
    visit[i][j]= 0
    cnt=1
    while q:
        x,y = q.popleft()
        color = ground[i][j]
        for a in range(4):
            nx = x+dx[a]
            ny = y+dy[a]
            if 0<=nx<12 and 0<=ny<6 and visit[nx][ny]==-1:
                if ground[nx][ny] == color:
                    q.append((nx,ny))
                    visit[nx][ny] =0
                    cnt+=1
    if cnt>=4:
        for i in range(11,-1,-1):
            for j in range(6):
                if visit[i][j] == 0:
                    ground[i][j] = '.'
        check = True

        
def move():
    for i in range(10,-1,-1):
        for j in range(6):
            if ground[i][j] !='.':
                color = ground[i][j]
                tempx = i

                while(1):
                    nx = tempx+1
                    tempx = nx
                    if nx>11 or ground[nx][j]!='.':
                        break
                if nx!=i:
                    ground[i][j] = '.'
                    ground[nx-1][j] = color
cnt = 0
while(1):
    check = False
    for i in range(11,-1,-1):
        for j in range(6):
            if ground[i][j] !='.':
                bomb(i,j)
    if check == True:
        cnt+=1
        move()
    else:
        break
print(cnt)

