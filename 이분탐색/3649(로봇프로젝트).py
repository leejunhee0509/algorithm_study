import sys
while(1):
    try:
        x = int(sys.stdin.readline())
        N = int(sys.stdin.readline())
        x = x*10000000
        temp = []
        for _ in range(N):
            temp.append(int(sys.stdin.readline()))
        temp.sort()
        left = 0
        right = len(temp)-1
        answer = []
        check = -1
        while left<right:
            amount = temp[left] + temp[right]
            if amount > x:
                right-=1
            elif amount < x:
                left+=1
            else:
                answer = [temp[left],temp[right]] 
                break
        if len(answer)==0:
            print("danger")
        else:
            print("yes",answer[0],answer[1])
    except :
        break