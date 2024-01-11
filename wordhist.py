d = {}
sent = input("Please enter a sentence: ")
i = 0
j = 0

print(len(sent))
while i < len(sent):
    j = i
    print(j)
    while sent[j] != " ":
        j += 1
    word = sent[i:j]
    # print(word)
    # print(len(word))
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
    i = j + 1
        
print(d)