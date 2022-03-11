import sys

V,E = map(int,sys.stdin.readline().split())
parent = [0]*(V+1)
for i in range(V):
    parent[i] = i
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[a] = b
    else:
        parent[b] = a
edge = []
for _ in range(E):
    s,e,cost = map(int,sys.stdin.readline().split())
    edge.append((cost,s,e))
edge.sort()
total = 0
for i in range(E):
    cost,a,b = edge[i]
    if find_parent(parent,a)!= find_parent(parent,b):
        union(parent,a,b)
        total+=cost
print(parent)
print(total)