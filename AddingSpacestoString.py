s="LeetcodeHelpsMeLearn"

sp=[8,13,15]
l=list(s)
ind=0
for i in range(len(sp)):
    l.insert(sp[i]+ind,' ')
    ind+=1 
out="".join(map(str,l))
print(out)


print([0]+sp)
print(sp+[len(s)])

a=[]
for i, j in zip([0]+sp, sp+[len(s)]):
    a.append(s[i:j])
    a.append(' ')
c="".join(map(str,a))
print(c)