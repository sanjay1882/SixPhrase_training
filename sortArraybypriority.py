a=[3,1,2,4]
#solution1
c=0
for i in range(len(a)):
    if (a[i]%2) ==0:
        a[c],a[i]=a[i],a[c]
        c+=1
print(a)

#solution2
b=[a[i] for i in range(len(a)) if (a[i]%2)==0]
for i in range(len(a)):
    if (a[i]%2)==1:
        b.append(a[i])
print(b)
