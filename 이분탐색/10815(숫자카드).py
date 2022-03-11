import sys

N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
num.sort()
M = int(sys.stdin.readline())
num2 = list(map(int,sys.stdin.readline().split()))

def find(target):
    left = 0
    right = N-1
    while left<=right:
        mid = (left+right)//2
        if num[mid]==target:
            return 1
        elif num[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return 0
answer = []
for i in range(M):
    target = num2[i]
    print(find(target), end= " ")
    