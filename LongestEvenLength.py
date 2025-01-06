a="It is a pleasent day today"
#a="time to write great code"
arr=[]
out=[]
length=0
arr=a.split(" ")
for i in arr:
    if len(i) %2 ==0:
        out.append(i)
maxstring=max(out,key=len)
print(maxstring)  
    
    
