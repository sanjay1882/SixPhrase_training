items={"Pizza":200,"Burger":250,"Idly":50,"Dosa":60}
print("Menus")
s=1
sno={}
for i in items:
    print(s,":",i,"\t",items[i])
    sno[i]=s
    s+=1
print("'Y' to Continue Order \t 'C' to Cart \t 'N' to Cancel Order")
Sum=0
while True:
    a=input("'Y' 'N 'C' =")
    if a.lower() =="y":
        pr=int(input("Enter a Item No :"))
        for key, value in sno.items():
            if value == pr:
                Sum+=items[key]
        
    elif a.lower()=="c":
        if Sum >500:
            print("You have Discount of 10%")
            out=Sum*(10/100)
            Sum=Sum-out
            print("the Amount is :",Sum)
            break
        else:
            print("the Amount iS :",Sum)
            break
    elif a.lower()=="n" or a.lower()=="e" :
        break    
