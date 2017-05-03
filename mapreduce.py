def word_freq(text, word):
    return len(filter(lambda x: x == word, text))

def group_freq(text, words):
    return reduce(lambda a, b: a + b, [word_freq(text, w) for w in words])

def most_freq(text):
    d = {}
    
    for word in text:
        if word not in d:
            d[word] = 0
        else:
            d[word] += 1

    vals = d.values()
    mx = reduce(lambda a, b: a if a > b else b, vals)
    return d.keys()[vals.index(mx)]
    
f = open("cornishfeastsandfolklore.txt", "r")
text = f.read().strip().split()
text = [ x.strip().strip("\"*().,!:;\'-[]{}").lower() for x in text ]

print 'Amount of times "the" appears:'
print(word_freq(text, "the"))
print 'Amount of times "and" appears:'
print(word_freq(text, "and"))
print 'Amount of times "the" and "and" appears:'
print(group_freq(text, ["the", "and"]))
print 'Amount of times "the" and "and" and "of" appears:'
print(group_freq(text, ["the", "and", "of"]))
print 'Most frequent word:'
print (most_freq(text))
print 'Most frequent word besides "the":'
print (most_freq(filter(lambda x: x != "the", text)))
