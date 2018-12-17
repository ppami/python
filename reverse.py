atext = "Hello there"


def reverse_letters(text):
    sth = ""
    for w in range(len(text) - 1, -1, -1):
        sth += text[w]
    return sth


print(reverse_letters(atext))

def reverse_sentence(text):
    #txt = text.split()
    new = []
    for w in range(len(text.split())-1, -1, -1):
        new.append(text[w])
    print(" ".join(new))



print(reverse_sentence(atext))

sentence = "Hello there"
print((" ".join(sentence.split()[::-1])))
print(" ".join(list(reversed(sentence.split()))))
