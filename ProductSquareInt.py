a=[1,3,1,0,0]
pro=1
for i in range(len(a)):
    if a[i]!=0:
        sq=a[i]**2
        pro*=sq
print(pro)