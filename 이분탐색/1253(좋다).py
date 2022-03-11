import sys

N = int(input())
num = list(map(int,sys.stdin.readline().split()))
num.sort()
answer = 0
for i in range(N):
    temp = num[:i]+num[i+1:]
    left = 0
    right = len(temp)-1
    while left<right:
        if temp[left]+temp[right]<num[i]:
            left+=1
        elif temp[left]+temp[right]>num[i]:
            right -=1
        else:
            answer+=1
            break
print(answer)
