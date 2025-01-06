def pangram(sentence):
    letters=set("abcdefghijklmnopqrstuvwxyz")
    sentence= sentence.lower()
    return letters.issubset(set(sentence))



if __name__ =="__main__":
    sen="The quick brown fox jumps over the lazy dog"
    #sen="A randomly generated pangram."
    a=int(input("Range"))
    list=[]
    for i in range(1,a+1):
        b=input("Enter")
        list.append(b)
    for i in list:
        if pangram(i):
            print("1",end='\t')
        else:
            print("0",end='\t')
        

        