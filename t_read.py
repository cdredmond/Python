d = {}

wfile = open('words.txt','r')
# create buckets of words that differ by one letter
for line in wfile:
    print(line)
    word = line[:-1]
    print(word)
    for i in range(len(word)):
        bucket = word[:i] + '_' + word[i+1:]
        if bucket in d:
            d[bucket].append(word)
        else:
            d[bucket] = [word]

iter(d.values())
