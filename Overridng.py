class comparater:
    def compare(self,a:int,b:int) ->bool:
        return a==b
    def compare(self,a:str,b:str) ->bool:
        return a==b
    def compare(self,a:list[int],b:list[int]) ->bool:
        if len(a)!=len(b):
            return False
        for i in range(len(a)):
            if a[i]!=b[i]:
                return False
        return True
    
if __name__ == "__main__":
    a=int(input("Enter a Range:"))

    comparater=comparater()
    
    for i in range(1,a+1):
        i=int(input("Enter"))
        if i==1:
            in1=input("Enter a string 1").strip()
            in2=input("Enter a string 2").strip()
            if comparater.compare(in1,in2):
                print("Same")
            else:
                print("Not Same")
            
    
        elif i==2:
            in1=int(input())
            in2=int(input())
            if comparater.compare(in1,in2):
                print("Same")
            else:
                print("Not Same")
        