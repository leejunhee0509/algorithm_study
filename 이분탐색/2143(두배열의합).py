import sys
from collections import defaultdict
T = int(input())
a = int(input())
listA = list(map(int,sys.stdin.readline().split()))
b= int(input())
listB = list(map(int,sys.stdin.readline().split()))

dic = defaultdict(int)
answer = 0

for i in range(a):
    for j in range(i,a):
        dic[sum(listA[i:j+1])] +=1
for i in range(b):
    for j in range(i,b):
        answer += dic[T-sum(listB[i:j+1])]
print(answer)