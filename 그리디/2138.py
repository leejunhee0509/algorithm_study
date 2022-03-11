import sys
import copy
from math import inf
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().strip()))
B = list(map(int,sys.stdin.readline().strip()))

def two(i,j,arr):

    arr[i] = 1-arr[i]
    arr[j] = 1-arr[j]


def three(i,j,k,arr):
    arr[i] = 1-arr[i]
    arr[j] = 1-arr[j]
    arr[k] = 1-arr[k]

answer = inf
for i in range(2):
    cnt = 0
    if i==0:
        r1 = copy.deepcopy(A)
        for j in range(N):
            if j==0 and r1!=B:
                    two(j,j+1,r1)
                    cnt+=1
            elif 1<=j<N-1:
                if r1[j-1]!=B[j-1]: 
                    three(j-1,j,j+1,r1)
                    cnt+=1
            else:
                if r1[j-1]!=B[j-1]:
                    two(j-1,j,r1)
                    cnt+=1
        if r1==B:
            answer = min(answer,cnt)
    else:
        r2= copy.deepcopy(A)
        for j in range(1,N):
            if 1<=j<N-1:
                if r2[j-1]!=B[j-1]:
                    three(j-1,j,j+1,r2)
                    cnt+=1
            else:
                if r2[j-1]!=B[j-1]:
                    two(j-1,j,r2)   
                    cnt+=1
        if r2==B:
            answer = min(answer,cnt)
      
print(answer)
    