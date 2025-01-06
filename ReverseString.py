

a=[4,4,6,2,6,4,9,8]
i=0
j=len(a)-1
while i<=j:
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1

print(a)
