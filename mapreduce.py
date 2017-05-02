def word_freq(text, word):
    ftext = filter(lambda x: x == word, text)
    return len(ftext)

def group_freq(text, words):
    return reduce(lambda a, b: a + b, [word_freq(text, w) for w in words])

def most_freq(text):
    
f = open("cornishfeastsandfolklore.txt", "r")
text = f.read().strip().split(" ")

print(word_freq(text, "the"))
print(word_freq(text, "and"))
print(group_freq(text, ["the", "and"]))
