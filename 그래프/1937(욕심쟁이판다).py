import sys
sys.setrecursionlimit(10**9)
N = int(input())
ground = []
for _ in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if dp[x][y] : return dp[x][y]
    dp[x][y]=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if ground[nx][ny]> ground[x][y]:
                dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]
    
result = 0
dp = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        result = max(dfs(i,j), result)     
print(result)