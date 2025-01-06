a=[2,2,4,5,6]
#a=[1,2,3,3]
f=a[0]
l=a[-1]
b=[]

for i in range(1,len(a)):
    if f==a[i]:
        if a[i-2] < a[i]:
            if f<=a[i]+1:
                b.append(f)
                b.append(a[i]-1)
                break
        elif a[i+2] >=a[i]:

            if f>=a[i]+1:
                b.append(f)
                b.append(a[i]+1)
                break
    f=a[i]
print(b)