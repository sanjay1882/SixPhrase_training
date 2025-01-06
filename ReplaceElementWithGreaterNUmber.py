arr=[17,18,5,4,6,1]
rightmax=-1
for i in range(len(arr)-1,-1,-1):
    tempmax=max(rightmax,arr[i])
    arr[i]=rightmax
    rightmax=tempmax

print(arr)