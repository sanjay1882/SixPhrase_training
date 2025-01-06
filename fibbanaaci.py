a=10
dp=[0]*a
dp[0]=0
dp[1]=1

for i in range(2,len(dp)):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[-1])