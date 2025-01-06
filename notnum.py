import re
a=list("hello0&/")
#isnumeric()
#isalpha()
for i in range(len(a)):
    if a[i].isalpha():
        print(a[i])
        
    else:
        continue
words = re.findall(r'\b\w+\b', "Hello, world! Welcome to Python.")
print(words)  # Output: ['Hello', 'world', 'Welcome', 'to', 'Python'