
def canJump(nums):
    f=len(nums)-1
    for i in range(len(nums)-2,-1,-1):
       if nums[i]+i>=f:
           f=i
    if f==0:
        print("True")
    else:
       print(" False")

nums=[3,2,1,0,4,6]
canJump(nums)
