import sys
from math import inf
N = int(sys.stdin.readline())
liquid = list(map(int,sys.stdin.readline().split()))
liquid.sort()
left= 0
right = N-1
answer = []
check = inf
while left< right:
    temp = abs(liquid[left]+liquid[right])
 
    if temp==0:
        answer = [liquid[left],liquid[right]]
        break
    if temp<check:
        answer = [liquid[left], liquid[right]]
        check = temp
    if liquid[left]+liquid[right] >0:
        right-=1
    elif liquid[left]+liquid[right]<0:
        left+=1

for x in answer:
    print(x,end= " ")