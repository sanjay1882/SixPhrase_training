a=[1,2,5,73,3,7,5]
b=int(input())
ptr=0

for i in range(0,len(a)):
    if a[i]==b:
        continue
    else:
        a[ptr]=a[i]
        ptr+=1
print(a)