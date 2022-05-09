def climbStairs(self, n: int) -> int:
    step = [0,1,2]

    #s[4]= 1,1,1,1 1,2,1, 2,1,1 n-2의 개수 + n-1의 개수같은..
    #1,1,2, 2,2, 

    #s[1]= 1
    #s[2]= 2
    #s[3]= 3
    #s[4]= 5 가설이 맞는거 같당. 피보나치 수열 문제인거 같다

    for s in range(3,n+1):
        step.append(step[s-1] + step[s-2])

    return step[n]

