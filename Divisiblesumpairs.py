
list=[2,4,67,8,9]
k=int(input("Enter a Number K"))
count=0




for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if (list[i]+list[j]) % k == 0:
            count+=1
print(count)
