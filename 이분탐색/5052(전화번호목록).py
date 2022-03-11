import sys

T = int(input())
for _ in range(T):
    N = int(input())
    ground = []
    for _ in range(N):
        ground.append(str(sys.stdin.readline()))
    ground.sort()
    flag = True
    for i in range(N-1):
        l = len(ground[i])-1
        if ground[i][:-1] in ground[i+1][:l]:
            print("NO")
            flag = False
            break
    if flag == True:
        print("YES")