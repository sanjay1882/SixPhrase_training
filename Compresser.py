a="AAAAAARRRRXXAAAAAAAAAATRRRR"

pointer=a[0]
l=[]
s=0
for i in range(len(a)):
    if a[i]==pointer:
        s=s+1
    else:
        if s >1:
            st=str(s)+pointer
            l.append(st)
        else:
            l.append(pointer)
        pointer=a[i]
        s=1
if s >1:

    st = str(s) + pointer
    l.append(st)
else:
    l.append(pointer)

out="".join(map(str,l))

print(out)
       



