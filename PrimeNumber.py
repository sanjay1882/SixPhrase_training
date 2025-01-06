import math
def PrimeNumber(num):
    for i in range(2,int(math.sqrt(num))+1):
        if (num%i)==0:
            return False
    return True




def Iterate_Prime_Num(start,end):
    for i in range(start,end+1):
        if PrimeNumber(i):
            print(i,end=' ')
        

    







print(Iterate_Prime_Num(1,100))