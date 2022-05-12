def countBits(self, n: int) -> List[int]:
    dp=[0]
    for i in range(1, n+1):
        #짝수인 경우, i//2 전거에서 0만 추가, 1개수 동일. 
        #홀수인 경우, i//2 전거에서 1추가.
        dp.append(dp[i // 2] + i % 2)
    return dp
