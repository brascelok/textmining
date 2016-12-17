# -*- coding: utf-8 -*-

with open('C:\\Users\\brascelok\\Desktop\\srilm-master\\brown-train.txt') as f:
    corpus = f.read()
    corpus = corpus.split()
    vocal = []
    for word in corpus:
        print(word + '\n')
        if word not in vocal:
            vocal.append(word)
    vocal.sort() # sorts normally by alphabetical order
    vocal.sort(key=len, reverse=False) # sorts by descending length
with open('C:\\Users\\brascelok\\Desktop\\srilm-master\\brown-train-vocab.txt', 'w') as f:
    for word in vocal:
        f.write(word + '\n')
