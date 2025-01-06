nums=[2,7,9,3,1]
dp=[0]*len(nums)

dp[0]=nums[0]
dp[1]=max(dp[0],dp[1])
for i in range(2,len(nums)):
    dp[i]=max(dp[1]+dp[-2],dp[-1])
print(dp[-1])



