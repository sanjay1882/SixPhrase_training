"""arr=[[1,3,2],
     [4,5,2],
     [2,4,3]]"""
"""arr=[
    [1,5,3],
    [1,5,1],
    [6,6,5]
]"""
arr=[
    [1,3,2],
    [4,5,2],
    [1,5,5]
]
dp=[0]*len(arr)
dp[0]=arr[0][2]
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[i][1] < arr[j][1]:
            dp[j]= arr[j][2]+dp[i]
        
print(dp[2])