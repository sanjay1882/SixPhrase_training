s="LeetcodeHelpsMeLearn"
a=[8,13,15]

b=[0]+a
c=a+[len(s)]


    
out=" ".join(s[i:j] for i,j in zip(b,a))
print(out)