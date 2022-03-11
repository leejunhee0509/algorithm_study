import sys
N = int(input())
circle = []
for i in range(N):
    point, r = map(int,sys.stdin.readline().split())
    a = point - r
    b = point + r
    circle.append((a,i,0))
    circle.append((b,i,1))
    
circle.sort()
stack = []
for i in range(len(circle)):
    fir = circle[i][2]
    if fir ==0:
        stack.append((circle[i]))
    else:
        if stack[-1][2]==0:
            if stack[-1][1] == circle[i][1]:
                stack.pop()
            else:
                print("NO")
                exit()
print("YES")