from ast import Return
import sys

N,M = map(int,sys.stdin.readline().split())
tall_graph = {}
short_graph = {}
for i in range(1,N+1):
    tall_graph[i] = set()
    short_graph[i] = set()
for _ in range(M):
    B,S = map(int,sys.stdin.readline().split())
    tall_graph[B].add(S)
    short_graph[S].add(B)

for i in range(1,N+1):
    for short in tall_graph[i]:
        short_graph[short].update(short_graph[i])
    for tall in short_graph[i]:
        tall_graph[tall].update(tall_graph[i])       
cnt = 0
for i in range(1,N+1):
    if len(tall_graph[i]) + len(short_graph[i]) == N-1:
        cnt+=1
print(cnt)