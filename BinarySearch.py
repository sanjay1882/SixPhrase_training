a=[-1,0,2,4,7,9,13]
l=0
r=len(a)-1
t=13
while l<=r:
    m=(l+r)//2 
    if a[m]==t:
        print(m)
        break
    elif t < r:
        r=m-1
    elif t >l:
        l=m+1

  
