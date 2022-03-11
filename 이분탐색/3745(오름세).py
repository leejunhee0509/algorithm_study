import sys

while(True):
    N = sys.stdin.readline()
    if not N:
        break
    N = int(N)
    money = list(map(int,sys.stdin.readline().split()))
    temp = [1]*N
    for i in range(N-2,-1,-1):
        if money[i]<money[i+1]:
            temp[i]+=temp[i+1]
    print(max(temp))
