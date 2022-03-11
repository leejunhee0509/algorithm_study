import sys
sys.setrecursionlimit(10**6)
N,M = map(int,sys.stdin.readline().split())

parent = [i for i in range(N)]

def find(x):
    if parent[x]!= x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(M):
    s,e = map(int,sys.stdin.readline().split())
    if find(s) != find(e):
        union(s,e)
    else:
        print(i+1)
        exit()
print(0)