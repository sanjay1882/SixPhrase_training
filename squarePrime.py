
def Prime(num):
    if num<=1:
        return False
    for i in range(2,(num//2)):
        if (num%i)==0:
            return False
    return True
    
def Prod_prime(arr):
    pr=0
    for i in range(len(arr)):
        if Prime(arr[i]):
            pr+=arr[i]**2
    return pr
a=[2,8,5]
print(Prod_prime(a))
