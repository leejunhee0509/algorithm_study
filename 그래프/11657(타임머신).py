import sys
from math import inf
import heapq
N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(M):
    S,E,T = map(int,sys.stdin.readline().split())
    graph.append((S,E,T))
    
def bellmanford(start):
    dist = [inf]*(N+1)
    dist[start] = 0
    check = True
    for i in range(N):
        for u,v,w in graph:
            if dist[u]!=inf and dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
                if i==N-1:
                    print(-1)
                    check = False
                    exit()
    if check == True:
        for i in range(2,N+1):
            if dist[i] == inf:
                print(-1)
            else:
                print(dist[i])
bellmanford(1)

    
        