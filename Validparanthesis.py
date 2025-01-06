s=input()
d={"{":"}","(":")","[":"]"}
st=[]
for i in s:
    if i in d.keys():
        st.append(i)
    else:
        if st==[]:
            print("False")
        else:
            if i ==d[st[-1]]: 
                st.pop()
            else:
                print("false")


if st==[]:
    print("True")
else:
    print("False")
        
        


