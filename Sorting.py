"""a=[10,20,39,1,797]
for i in range(len(a)-1):
    for j in range(i+1,len(a)-1):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
   
print(a)""" #buubleSort


"""a=[10,20,39,1,797]
for i in range(len(a)-1):
    min=i
    for j in range(i+1):
        if a[j] < min:
            min=a[j]
            a[i],a[j]=a[j],a[i]
print(a)"""#Selection Sort