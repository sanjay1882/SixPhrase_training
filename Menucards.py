items={"Pizza":200,"Burger":250,"Idly":50,"Dosa":60}
print("Menus")
s=1
sno={}
for i in items:
    print(s,":",i,"\t",items[i])
    sno[i]=s
    s+=1
print("'Y' to Continue Order")
print("'N' to Cancel Order")
print("'C' to Cart")

Sum=0
while True:
    a=input("Enter:")
    if a.lower() =="y":
        pr=int(input("Enter a Item No :"))
        for key, value in sno.items():
            if value == pr:
                Sum+=items[key]
        
    elif a.lower()=="c":
        if Sum >500:
            print("You have Discount of 10%")
            out=Sum*(10/100)
            sum=sum-out
            print("the Amount is :",sum)
    elif a.lower()=="n" or a.lower()=="e" :
        break    








