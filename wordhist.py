d = {}
sent = input("Please enter a sentence: ")
i = 0
j = 0
length = len(sent)

while i < length:
    j = i
    while sent[j] != " ":
        j += 1
        if j >= length: break

    word = sent[i:j]
    
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
    i = j + 1
        
print(d)