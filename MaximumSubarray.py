arr=[7,2,5,10,8]
Max=0
curr=0
ar=[]
ma=[]
for i in arr:
    curr=curr+i
    ar.append(i)
    
    if curr < 0:
        curr=0
        ar.clear()
    if curr >Max:
        Max=curr
        ma=ar.copy()
print(Max,ma)

    

    