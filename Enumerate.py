a=[1,3,4,5,6]
b=[1,3,4,5,6]

for i in zip(a,b):
    print(i[0]+i[1])

for i in reversed(a):
    print(i)


for i in enumerate(a,2):
    print(i)


try:
    a=10
    n="hello"
    print(a+n)

except Exception as e:
    print("An error occured in your code:\t",e)
    
finally:
    print("end of code")