a=[2,4,5,6,7]
b=len(a)
s=sum(range(1,b+1))
print(s-sum(a))
def missing_number(arr, n):
    return sum(range(1, n+1)) - sum(arr)
print(missing_number(a, b))