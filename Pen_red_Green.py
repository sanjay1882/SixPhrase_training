a=[2,1,3,4,6]
count=0
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
      if (a[i]%2)==1 and (a[j]%2)==0 :
        count+=1
print(count)
        
