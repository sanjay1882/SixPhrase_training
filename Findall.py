import re
string = "abababa123"

a=re.findall('\d',string)
print(a)
for i in range(len(a)):
    string.replace(a[i],'')

print(string)


