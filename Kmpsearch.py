def kmp_search(text, pattern):
    lps = [0] * len(pattern)
    j = 0
   

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
        elif j > 0:
            j = lps[j - 1]
            i -= 1
    i, j = 0, 0

    
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    return -1
print(kmp_search("ababcababc", "abc")) 