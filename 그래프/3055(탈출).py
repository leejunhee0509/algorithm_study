import sys
from collections import deque

R,C = map(int,sys.stdin.readline().split())
ground =[]
water = deque()
animal = deque()
visit = [[-1]*C for _ in range(R)]

for i in range(R):
    ground.append(list(sys.stdin.readline().strip()))
    for j in range(C):
        if ground[i][j] == 'S':
            animal.append((i,j))
            ground[i][j] = '.'
            visit[i][j] = 0
        elif ground[i][j] == 'D':
            end = [i,j]
        elif ground[i][j] == '*':
            water.append((i,j))  
dx = [-1,1,0,0]
dy = [0,0,1,-1]
cnt = 0
def find():
    global cnt
    while(1):
        waterlen = len(water)
        while waterlen>0:
            x,y = water.popleft()
            waterlen -=1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<R and 0<=ny<C and ground[nx][ny] == '.':
                    ground[nx][ny] = '*'
                    water.append((nx,ny))
        alen = len(animal)
        if alen == 0:
            print("KAKTUS")
            break
        while alen>0:
            x,y = animal.popleft()
            alen-=1
            for i in range(4):
                nx = x+dx[i]
                ny = y +dy[i]
                if 0<=nx<R and 0<=ny<C:
                    if ground[nx][ny] == '.' and visit[nx][ny] == -1:
                        animal.append((nx,ny))
                        visit[nx][ny] = 0
                    elif ground[nx][ny] == 'D':
                        print(cnt+1)
                        return
        cnt+=1
find()