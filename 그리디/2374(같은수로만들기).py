import sys

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
cnt = 0
while(1):
    for x in sorted(num):
        if x!=sorted(num)[0]:
            next = x ##next는 두번쨰로 작은수
            break
    amount = next-min(num) ##제일 작은수와 두번쨰로 작은수의 차이
    if min(num) == max(num): ##num에 들어있는 최솟값과 최댓값이 같으므로 모두 같은수, 즉 break
        print(cnt)
        break
    target = min(num) #num에서 가장 작은 수 부터 더해감
    index = 0
    count = 0 #num에서 제일작은수가 연속으로 있는 구간
    while(index<N):  
        if num[index] == target: ##num 배열에서 target과 같은값을 찾음
            count+=1
            right = index+1
            num[index] +=amount
            for j in range(right,N,1):
                if num[j]==target:
                    num[j]+=amount
                    index = j
                else:
                    break
        index+=1
    cnt+=count*amount