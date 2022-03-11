import sys
N = int(input())
temp = list(map(str,sys.stdin.readline().strip()))
stack = []
visit = [0]*N
for i in range(N):
    if temp[i]=="(":
        stack.append(i)
    else:
        if(stack):
            point = stack.pop()
            visit[point]=1
            visit[i] = 1
count = 0
answer = 0
for number in visit:
    if number==1:
        count+=1
        answer = max(answer,count)
    else:
        count=0
print(answer)