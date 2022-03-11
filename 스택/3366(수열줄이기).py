import sys
N,M,x,y,K = map(int,sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))
print(ground)