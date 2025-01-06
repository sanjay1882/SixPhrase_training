import re
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit. "
banned = ["hit"]

r=re.findall(r'\w+',paragraph.lower())
print(r)
s=set(banned)
out=Counter(word for word in r if word not in s)
print(out)
print(max(out,key=out.get))
