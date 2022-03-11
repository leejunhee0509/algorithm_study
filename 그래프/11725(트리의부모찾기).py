import sys
from collections import deque
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    S,E = map(int,sys.stdin.readline().split())
    tree[S].append(E)
    tree[E].append(S)

answer = [-1]*(N+1)
q= deque()
q.append(1)
visit = [-1]*(N+1)
visit[1] = 0
while q:
    parent = q.popleft()
    for node in tree[parent]:
        if visit[node] == -1:
            q.append(node)
            visit[node] = 0
            answer[node] = parent
for i in range(2,N+1):
    print(answer[i])