a="vijayajiv"
b=True
s=0
e=len(a)-1
if b:
    while s<e:
        if a[s]==a[e]:
            s+=1
            e-=1
        else:
            print("Not Palindrome")
            b=False
            break
            
if b:
    print("Panindrome")
