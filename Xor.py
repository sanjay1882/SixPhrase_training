nums=5
o=[]
start=0
for i in range(start,nums):
    o.append(start+2*i)
ins=0
out=1
for i in range(1,len(o)):
    out=o[ins]^o[i]
    ins+=1
print(out)