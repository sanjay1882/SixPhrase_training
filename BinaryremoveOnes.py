a=7875858
b=str(bin(a))[2:]

b=b.replace('11','')
print(b)

  #For strings
char='hello'
c=" ".join(format(ord(i),'08b') for i in char)
c=c.replace('11','')
print(c)

d="".join(format(ord(j),'08b') for j in char)
print(d)