arr=[32,232,434,1,3,2,34,61]
num_to={}
nums=sorted(set(arr)) #sort set and convert to list

rank=1

for num in nums:
    num_to[num]=rank
    rank+=1


for i in range(len(arr)):
    arr[i]=num_to[arr[i]]#assigning the Key value

print(arr)