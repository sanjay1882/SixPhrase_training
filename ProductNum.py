#Product Odd numbers

a=[2,4,3,3]
sum=1
for i in range(len(a)):
    if (a[i]%2)==1:
        sum*=a[i]
print(sum)