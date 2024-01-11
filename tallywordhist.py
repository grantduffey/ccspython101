d = {}
sent = input("Please enter a sentence: ")
i = 0
j = 0
k = 0
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


d = sorted(d.items(), key=lambda d: d[1], reverse = True)

print("The top three words are:")

for x in d:
    print("%s: %d" % (x[0], x[1]))
    k += 1
    if k > 2: break

# to be or not to be do be do be do