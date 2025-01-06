

def Swap(s1,s2):
   
   
    for i in range(len(s1)):
        for j in range(i+1):
            s1[j],s2[j]=s2[j],s1[j]
            

    return "".join(map(str,s1))
s1=list("29152")
s2=list("10523")
print(Swap(s2.copy(),s1.copy()))
print(Swap(s1.copy(),s2.copy()))
