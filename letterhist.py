d = {}
word = input("Please enter a word: ")

for i in range(len(word)):
    if word[i] in d:
        d[word[i]] += 1
    else:
        d[word[i]] = 1

print(d)