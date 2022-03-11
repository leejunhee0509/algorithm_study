import sys

R,C = map(int,sys.stdin.readline().split())
ground = []
for _ in range(R):
    ground.append(list(map(str,sys.stdin.readline().strip())))
dx = [-1,0,1]
visit = [[-1]*C for _ in range(R)]

def dfs(x,y):
    if y==C-1:
        return True
    for i in range(3):
        nx = x+dx[i]
        ny = y+1
        if 0<=nx<R and ground[nx][ny]=='.' and visit[nx][ny]==-1:
            visit[nx][ny]=0
            if dfs(nx,ny):
                return True
    return False
answer = 0
for i in range(R):
    if ground[i][0]=='.':
        if dfs(i,0):
            answer+=1
print(answer)