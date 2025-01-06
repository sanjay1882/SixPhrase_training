from collections import Counter
a="helloo"
b=Counter(a)
for i in a:
    if b[i]==1:
        print(i)
        break
    else:
        continue
