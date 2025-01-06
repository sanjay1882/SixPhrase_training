d=["RG","GR","RG","GR","RR","GG"]

g=set(d)
b=[d[i] for i in range(0,len(d)) if d[i][-1] ==d[i][0]]
print(b)