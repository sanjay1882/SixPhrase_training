expiryLimit = 4
commands = [[0,1,1], [0,2,2], [1,1,5],[1,2,7]]
"""
expiryLimit = 3
commands = [[0, 1, 1], [1, 1, 5]]

expiryLimit = 3
commands = [[0,1,1],[1,1,4],[1,2,5]]
"""
dict={}
sum=0
for i in commands:
    if i[0]==0:
        dict[i[1]]=i[2]+expiryLimit
    else:
        if i[1] in dict.keys():
            if i[2] >= dict[i[1]]:
                dict[i[1]]=i[2]+expiryLimit
val = max(dict.values())
for s in dict.values():
    if s>=val:
        sum+=1

print(sum)
