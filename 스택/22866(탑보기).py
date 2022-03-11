import sys

N = int(input())
building = list(map(int,sys.stdin.readline().split()))
stackl = []
stackr = []
info = [[] for _ in range(N)]
for i in range(N):
    while stackl:
        height = stackl[-1][0]
        index = stackl[-1][1]
        if height<=building[i]:
            stackl.pop()
        else:
            dist = i-index+1
            info[i].append((dist,index,len(stackl)))
            stackl.append((building[i],i+1))
            break
    if len(stackl)==0:
        stackl.append((building[i],i+1))
for i in range(N-1,-1,-1):
    while stackr:
        height = stackr[-1][0]
        index = stackr[-1][1]
        if height<=building[i]:
            stackr.pop()
        else:
            dist = -(i-index+1)
            info[i].append((dist,index,len(stackr)))
            stackr.append((building[i],i+1))
            break
    if len(stackr)==0:
        stackr.append((building[i],i+1))

for i in range(len(info)):
    x = info[i]
    if len(x)==0:
        print(0)
    else:
        x.sort(key=lambda x:(x[0],x[1]))
        if len(x)==1:
            print(x[0][2],x[0][1])
        else:
            print(x[0][2]+x[1][2],x[0][1])
        