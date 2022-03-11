import sys

V,E = map(int,sys.stdin.readline().split())
parent = [i for i in range(V+1)]

def find(parent,a):
    if parent[a] !=a:
        parent[a] = find(parent,parent[a])
    return parent[a]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

info = []
for _ in range(E):
    a,b,cost = map(int,sys.stdin.readline().split())
    info.append((cost,a,b))
info.sort()
total = 0
for cost,S,E in info:
    if find(parent, S)!=find(parent, E):
        union(parent,S,E)
        total += cost

print(total)