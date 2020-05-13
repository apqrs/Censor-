

def word_index(sent, word):
    b = []
    start = 0
    n = 0
    while n != -1:
        n = sent.find(word, start)
        b.append(n)
        start = n + len(word)
    return b[:-1]

print(word_index('she she she she','she'))
